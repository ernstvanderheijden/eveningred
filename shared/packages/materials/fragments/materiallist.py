import datetime

from configuration.models import Configuration
from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from materials.models import Material

nameform = 'materialform'
crudname = 'crud'


class Materiallist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.onclick = "do_url('" + self.fragment + "', " + str(int(self.level) + 1) + ", '/core/update/pk_replace/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=" + crudname + "&fk=&pk=pk_replace&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded) + "')"
        self.order_by = "-issuedate"
        self.paginatesize_overwrite = ''
        self.displayfield = 'description'
        if request.user.has_perm('materials.add_material'):
            self.tools.update({
                'create': {
                    "title": "fas fa-plus",
                    "tooltype": "create",
                    "class": "btn btn-success",
                    "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
                },
            })
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "issuedate": {
                "caption": "Uitgiftedatum",
                "fieldtype": "date",
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
            "customerid__relationname": {
                "caption": "Leverancier",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "purchasingcosts": {
                "caption": "Bedrag",
                "fieldtype": "decimal",
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
        self.records = Material.objects.filter(userid=request.user.id, processdate__isnull=True).values(*self.columnfields.keys(), "id")
