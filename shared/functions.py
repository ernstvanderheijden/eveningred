from master.models import Vattype


def nonetozero(value):
    # Convert None to int zero else return value.
    if value is None:
        return 0
    return value


def booleantotext(value):
    match value:
        case True:
            return "Ja"
        case False:
            return "Nee"
        case _:
            return "Onbepaald"


def list_to_string(a_list):
    return str(a_list).replace('[', '').replace(']', '').replace(' ', '')


# def create_hosts(request):
#     http_hosts = list()
#     domains = Domain.objects.filter(tenant_id=request.tenant.id).values('domain')
#     for domain in domains:
#         if domain['domain'] == 'localhost':
#             http_hosts.append('http://localhost:8000')
#         else:
#             http_hosts.append('https://' + domain['domain'])
#     return http_hosts


def get_fullname(first_name, insertion, last_name):
    return f"{first_name or ''}{' ' if first_name else ''}" \
           f"{insertion or ''}{' ' if insertion else ''}" \
           f"{last_name or ''}"


def get_fulladdress(street, number, suffix, postalcode, city):
    if street:
        return f"{street or ''}{' ' if street else ''}" \
               f"{number or ''}" \
               f"{suffix or ''},{' ' if number else ''}" \
               f"{postalcode or ''}{' ' if postalcode else ''}" \
               f"{city or ''}"
    else:
        return ''


def get_crud_contenttitle(viewtype):
    match viewtype:
        case 'create':
            return 'Nieuw'
        case 'update':
            return 'Wijzig'
        case 'delete':
            return 'Verwijder'


# def create_new_record(request):
#     fk = request.GET.get('pk', '')
#     linkitem = request.GET.get('linkitem', '')
#     linkid = 0
#     if linkitem:
#         linkid = int(request.GET.get('linkid'))
#
#     if request.GET.get('fragment', '') == 'contractlinelist':
#         record = Contractline()
#         record.contractid_id = fk
#         articles = Article.objects.filter(id=linkid)
#         articles = articles.values('description', 'estatetypeid_id', 'handlingtype', 'unittypeid_id', 'unittypeid__unit', 'price', 'id', 'vattypeid_id', 'unittypeid_id',
#                                    'vattypeid__percentage', 'is_on_final_invoice')
#         for article in articles:
#             record.articleid_id = article['id']
#             record.price = article['price']
#             contract = Contract.objects.get(id=fk)
#             nr_contractlines = Contractline.objects.filter(contractid_id=contract.id).count()
#             orderingid = nr_contractlines
#             dict_schemas = dict_invoiceschemas()
#
#             add_single_contractline(contract, article, orderingid, dict_schemas)
#             if contract.contracttypeid.key == 'rental_recurring' and contract.startdate.day != 1 and article['handlingtype'] == 'rent':
#                 enddate = contract.startdate + relativedelta(months=1)
#                 contract.enddate = date(enddate.year, enddate.month, 1)
#
#                 articles = Article.objects.filter(estatetypeid_id=article['estatetypeid_id'], handlingtype='rent_broken_month')
#                 articles = articles.values('description', 'estatetypeid_id', 'handlingtype', 'unittypeid__unit', 'price', 'id', 'vattypeid_id', 'unittypeid_id',
#                                            'vattypeid__percentage', 'is_on_final_invoice')
#                 for article_extra in articles:
#                     # orderingid = orderingid + 1
#                     add_single_contractline(contract, article_extra, orderingid, dict_schemas)
#
#     elif request.GET.get('fragment', '') == 'invoicelinelist':
#         record = Invoiceline()
#         record.invoiceid_id = fk
#         articles = Article.objects.filter(id=linkid)
#         articles = articles.values('estatetypeid_id', 'handlingtype', 'unittypeid_id', 'unittypeid__unit', 'price', 'id', 'vattypeid_id', 'unittypeid_id', 'description',
#                                    'vattypeid__percentage', 'is_on_final_invoice')
#         for article in articles:
#             record.articleid_id = article['id']
#             record.price = article['price']
#             invoice = Invoice.objects.get(id=fk)
#             nr_invoicelines = Invoiceline.objects.filter(invoiceid_id=invoice.id).count()
#             orderingid = nr_invoicelines + 1
#             add_single_invoiceline(invoice, article, orderingid)


# def delete_the_record(request):
#     itemid = request.GET.get('itemid', '')
#
#     if request.GET.get('fragment', '') == 'contractlinelist':
#         Contractline(id=itemid).delete()
#     elif request.GET.get('fragment', '') == 'invoicelinelist':
#         invoice = Invoice.objects.get(id=int(request.GET.get('pk')))
#         reorder_invoicelines_on_pre_delete(invoice.id, itemid)
#         Invoiceline(id=itemid).delete()
#         calculate_totals_invoice(invoice)
#     elif request.GET.get('fragment', '') == 'cocustomerlist':
#         Cocustomer(id=itemid).delete()
#     else:
#         pass
#     return


def get_status(strmodel, a_variable):
    amount = None
    classcolor = ''
    statustext = ''
    if strmodel == 'Some_model':
        pass
    else:
        match a_variable:
            case 0:
                statustext = 'Actief'
                classcolor = "badge-warning"
            case -1:
                statustext = 'Inactief'
                classcolor = "badge-success"
    return [statustext, classcolor, amount]


def get_vatcode_from_percentage() -> dict:
    dict_vattypes = dict()
    vattypes = Vattype.objects.all()
    for vattype in vattypes:
        dict_vattypes.update({vattype.percentage: vattype.vatcode})
    return dict_vattypes


def get_percentage_from_vatcode() -> dict:
    dict_vattypes = dict()
    vattypes = Vattype.objects.all()
    for vattype in vattypes:
        dict_vattypes.update({vattype.vatcode: vattype.percentage})
    return dict_vattypes


def fill_data_with_print_records(data, response):
    data['print_records'] = response
    data['print_type'] = 'invoices'
    data['form_is_valid'] = True
    data['messagelist'] = ["Items verzonden, " + str(len(response)) + " items te printen", "success", "long"]
