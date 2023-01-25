from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from shared.api import get_mollie_payment
#
#
# @csrf_exempt
# # @login_required ( Not needed, while this def is a public one)
# def mollie_payment(request):
#     mollie_id = request.POST.get('id', None)
#     if mollie_id:
#         record = Invoice.objects.get(mollie_id=mollie_id)
#         payment_response = get_mollie_payment(mollie_id)
#         record.mollie_response['status'] = payment_response['status']
#         if record.mollie_response['status'] == "paid":
#             record.is_paid = True
#         else:
#             record.is_paid = False
#         record.save()
#     return HttpResponse('')
