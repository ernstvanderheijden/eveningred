import datetime

from configuration.models import Configuration
from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from hours.models import Hour

nameform = 'hourform'


class Hourlist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "-issuedate"
        self.paginatesize_overwrite = ''
        self.displayfield = 'description'
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        if request.user.has_perm('hours.add_hours'):
            self.tools.update({
                'create': {
                    "title": "fas fa-plus",
                    "tooltype": "create",
                    "class": "btn btn-primary",
                    "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
                },
            })
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "issuedate": {
                "caption": "Datum",
                "fieldtype": "date",
                "operator": "__icontains",
            },
            "amounthours": {
                "caption": "Aantal",
                "fieldtype": "decimal",
                "operator": "__icontains",
            },
            "description": {
                "caption": "Omschrijving",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "projectid__description": {
                "caption": "Project",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            # "userid__fullname": {
            #     "caption": "Gebruiker",
            #     "fieldtype": "char",
            #     "operator": "__icontains",
            # },
        }
        configuration = Configuration.objects.get(is_default=True)
        datefrom = datetime.datetime.today() - datetime.timedelta(days=configuration.days_history)
        self.records = Hour.objects.filter(userid=request.user.id, issuedate__gte=datefrom).values(*self.columnfields.keys(), "id")
