# import decimal
# from contracts.models import Contractline
# from core.functions.render_fragments import fragmentdatabuilder
# from core.globals.global_functions import clean_fields, decode_string
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import get_object_or_404, redirect
# from django.template.loader import render_to_string
# from django.views.decorators.csrf import csrf_exempt
# from invoices.models import Invoiceline, Invoice
# from pikepdf import Pdf
# from shared.api import get_mollie_payment
# from shared.contract import save_contract_contexttext, get_contract
# from shared.invoice import get_invoice
# from shared.master import save_master_blueprinttext
# from shared.pdf import get_ctx_pdf_invoice, create_pdf_from_ctx, download_or_open_pdf, get_ctx_pdf_contract
# from shared.utilityusage import save_utilityusages_batch
#
#
# def move_item(request):
#     data = dict()
#     rec_moving = ''
#     recordid = request.GET.get('recordid', '')
#     fragment = request.GET.get('fragment')
#     if fragment == 'contractlinelist':
#         rec_moving = Contractline.objects.get(id=recordid)
#     elif fragment == 'invoicelinelist':
#         rec_moving = Invoiceline.objects.get(id=recordid)
#     direction = request.GET.get('direction', '')
#     if direction == 'up':
#         rec_moving_new_orderingid = rec_moving.orderingid - 1
#     else:
#         rec_moving_new_orderingid = rec_moving.orderingid + 1
#     data['form_is_valid'] = True
#     if fragment == 'contractlinelist':
#         try:
#             # Give the orderingid to the rec_to_move record
#             rec_to_move = Contractline.objects.get(contractid_id=rec_moving.contractid_id, orderingid=rec_moving_new_orderingid)
#             rec_to_move.orderingid = rec_moving.orderingid
#             rec_to_move.f_updater = request.user
#             rec_to_move.save()
#             # Give the new orderingid to the rec_moving record
#             rec_moving.orderingid = rec_moving_new_orderingid
#             rec_moving.f_updater = request.user
#             rec_moving.save()
#         except (Contractline.DoesNotExist, AttributeError):
#             data['form_is_valid'] = False
#             return JsonResponse(data)
#     elif fragment == 'invoicelinelist':
#         try:
#             # Give the orderingid to the rec_to_move record
#             rec_to_move = Invoiceline.objects.get(invoiceid_id=rec_moving.invoiceid_id, orderingid=rec_moving_new_orderingid)
#             rec_to_move.orderingid = rec_moving.orderingid
#             rec_to_move.f_updater = request.user
#             rec_to_move.save()
#             # Give the new orderingid to the rec_moving record
#             rec_moving.orderingid = rec_moving_new_orderingid
#             rec_moving.f_updater = request.user
#             rec_moving.save()
#         except (Invoiceline.DoesNotExist, AttributeError):
#             data['form_is_valid'] = False
#             return JsonResponse(data)
#
#     data = fragmentdatabuilder(request, {})
#
#     return JsonResponse(data)
#
#
# def set_record_field(record, namefield):
#     if hasattr(record, 'amount'):
#         if not record.amount:
#             record.amount = 0
#     if hasattr(record, 'price'):
#         if not record.price:
#             record.price = 0
#     if hasattr(record, 'discount'):
#         if not record.discount:
#             record.discount = 0
#     # # Startdate or enddate
#     # if namefield == 'startdate' or namefield == 'enddate':
#     #     if record.startdate and record.enddate:
#     #         record.amount = (record.enddate - record.startdate).days
#     #         record.explanation = format(record.startdate, "%d-%m-%Y") + " tot " + format(record.enddate, "%d-%m-%Y")
#
#     return record
#
#
# @csrf_exempt
# @login_required
# def save_checkbox(request):
#     data = dict()
#     record = dict()
#     checked = request.POST.get('key')
#     if request.GET.get('package') == 'contracts' and request.GET.get('fragment') == 'contractlinelist':
#         record = get_object_or_404(Contractline, pk=request.GET.get("pk", ""))
#
#     namefield = request.GET.get('namefield', '')
#     if namefield and checked == 'true':
#         setattr(record, namefield, True)
#     elif namefield and checked == 'false':
#         setattr(record, namefield, False)
#
#     record.save()
#     data['messagelist'] = ["Item opgeslagen", "success", "short"]  # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
#     data['form_is_valid'] = True
#     return JsonResponse(data)
#
#
# @csrf_exempt
# @login_required
# def save_value(request):
#     data = dict()
#     record = dict()
#     strajax = request.POST.get('key')
#     invoice = 0
#     try:
#         strajax = strajax.replace(',', '.')
#         editable = True
#         if request.GET.get('package') == 'contracts' and request.GET.get('fragment') == 'contractlinelist':
#             record = get_object_or_404(Contractline, pk=request.GET.get("pk", ""))
#             if record.contractlineid_invoiceline.all() and record.handlingtype != 'utility_deposit':
#                 editable = False
#         elif request.GET.get('package') == 'invoices' and request.GET.get('fragment') == 'invoicelinelist':
#             record = get_object_or_404(Invoiceline, pk=request.GET.get("pk", ""))
#             invoice = Invoice.objects.get(id=record.invoiceid_id)
#             if invoice.status > 0:
#                 editable = False
#
#         if editable:
#             namefield = request.GET.get('namefield', '')
#             if namefield and strajax:
#                 setattr(record, namefield, strajax)
#             elif namefield:
#                 setattr(record, namefield, None)
#         else:
#             data['form_is_valid'] = False
#             data['messagelist'] = ["Niet opgeslagen", "danger"]
#             return JsonResponse(data)
#
#         strclean = clean_fields(record)  # clean all fields
#         if strclean:  # clean all fields
#             data['messagelist'] = [str(strclean).replace('[', '').replace(']', '').replace('"', ''), 'danger']
#             data['form_is_valid'] = False
#             return JsonResponse(data)
#         else:
#             record = set_record_field(record, namefield)
#             data['recordid'] = record.id
#             record.lineprice = calculate_lineprice(record)
#             if request.GET.get('fragment') == 'contractlinelist' or request.GET.get('fragment') == 'invoicelinelist':
#                 data['refresh_fields'] = {
#                     "price": "{:.2f}".format(record.price),
#                     "amount": "{:.2f}".format(record.amount),
#                     "discount": "{:.2f}".format(record.discount),
#                     "lineprice": "{:.2f}".format(record.lineprice),
#                     "explanation": record.explanation
#                 }
#             else:
#                 data['refresh_fields'] = ''
#             record.save()
#         if request.GET.get('package') == 'invoices' and invoice:  # Refresh invoice totals
#             invoice = Invoice.objects.get(id=invoice.id)
#             ctx = dict()
#             ctx['invoice'] = invoice
#             data['refresh_fields']['fragment'] = {'invoice_sum': render_to_string('shared/summary/invoice_totals_inner.html', {'ctx': ctx})}
#         data['messagelist'] = ["Item opgeslagen", "success", "short"]  # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
#         data['form_is_valid'] = True
#     except decimal.DivisionByZero:
#         data['messagelist'] = ["Foutieve invoer", "danger"]
#         data['form_is_valid'] = False
#     return JsonResponse(data)
#
#
# @csrf_exempt
# @login_required
# def save_record(request):
#     data = dict()
#     data['refresh_fields'] = dict()
#     strajax = request.POST.get('dict_fields_and_values')
#     strcontent = request.POST.get('content')
#     recordid = request.GET.get('recordid', '')
#     successurl = request.GET.get('successurl', '')
#     if successurl:
#         successurl = decode_string(successurl)
#         data['successurl'] = successurl
#     key: str
#     package = request.GET.get('package', '')
#     fragment = request.GET.get('fragment', '')
#     try:
#         if package == 'utilityusages' and fragment == 'utilityusagebatchlistprocess':
#             save_utilityusages_batch(request, data, strajax, recordid)
#         elif package == 'contracts' and fragment == 'contracttext':
#             save_contract_contexttext(request, data, strcontent)
#         elif package == 'master' and fragment == 'blueprinttext':
#             save_master_blueprinttext(request, data, strcontent)
#         else:
#             data['form_is_valid'] = False
#             data['messagelist'] = ["Niet opgeslagen", "danger"]
#             return JsonResponse(data)
#         # data['messagelist'] = ["Item opgeslagen", "success", "short"]
#         data['form_is_valid'] = True
#     except decimal.DivisionByZero:
#         data['messagelist'] = ["Foutieve invoer", "danger"]
#         data['form_is_valid'] = False
#     data['fragment'] = 'contractpreview'
#     return JsonResponse(data)
#
#
# def calculate_lineprice(record):
#     if record.discount:
#         lineprice = record.price * record.amount - (record.price * record.amount * record.discount / 100)
#     else:
#         lineprice = record.price * record.amount
#     return lineprice
#
#
# @csrf_exempt
# # @login_required ( Not needed, while this def is a public one)
# def check_mollie_status(request):
#     slug = request.GET.get('slug', None)
#     if slug:
#         record = Invoice.objects.get(slug=slug)
#         check_mollie_status_record(record)
#         return redirect('/core/template/?level=0&package=invoices&chapter=detail&pk=' + str(record.id))
#     return HttpResponse('')
#
#
# def check_mollie_status_record(record):
#     payment_response = get_mollie_payment(record.mollie_id)
#     old_mollie_status = record.mollie_response['status']
#     new_mollie_status = payment_response['status']
#     if old_mollie_status != new_mollie_status:
#         record.mollie_response['status'] = new_mollie_status
#         record.save()
#     return record
#
#
# def download_or_open_contracts(request, multiselect_records, download_or_open):
#     record = dict()
#     pdf = Pdf.new()
#     for recordid in multiselect_records:
#         record = get_contract(recordid, None)
#         ctx = get_ctx_pdf_contract(record)
#         create_pdf_from_ctx(pdf, ctx)
#     # return download_or_open_pdf(pdf, download_or_open, 'contract.pdf')
#     if len(multiselect_records) == 1:
#         return download_or_open_pdf(pdf, download_or_open, 'Contract' + ' ' + str((record['contractnumber'])) + '.pdf')
#     else:
#         return download_or_open_pdf(pdf, download_or_open, 'Contracten.pdf')
#
#
# def download_or_open_invoices(multiselect_records, download_or_open):
#     record = dict()
#     pdf = Pdf.new()
#     for recordid in multiselect_records:
#         record = get_invoice(recordid, None)
#         ctx = get_ctx_pdf_invoice(record)
#         create_pdf_from_ctx(pdf, ctx)
#     if len(multiselect_records) == 1:
#         return download_or_open_pdf(pdf, download_or_open, 'Factuur' + ' ' + str((record['invoicenumber'])) + '.pdf')
#     else:
#         return download_or_open_pdf(pdf, download_or_open, 'Facturen.pdf')
