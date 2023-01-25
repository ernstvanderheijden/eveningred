from core.globals.global_fragments import GlobalList
from configuration.models import Configuration
from core.globals.global_functions import encode_string

nameform = 'configurationform'


class Configurationlist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "-id"
        self.paginatesize_overwrite = ''
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.successurl_decoded = ""
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.tools = {
            'create': {
                "title": "fas fa-plus",
                "tooltype": "create",
                "class": "btn btn-primary",
                "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&fk=&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
            },
        }
        self.columnfields = {  # Fieldtypes are: boolean, char, date, applog, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "id": {
                "caption": "ID",
                "fieldtype": "number",
                "operator": "__icontains",
            },
            "created": {
                "caption": "Aangemaakt op",
                "fieldtype": "datetime",
                "operator": "__icontains",
            },
            "creatorid__first_name": {
                "caption": "Aangemaakt door",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "updated": {
                "caption": "Bijgewerkt op",
                "fieldtype": "datetime",
                "operator": "__icontains",
            },
            "updaterid__first_name": {
                "caption": "Bijgewerkt door",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "is_default": {
                "caption": "Standaard",
                "fieldtype": "boolean",
                "operator": "__icontains",
            },
        }
        self.records = Configuration.objects.filter().values(*self.columnfields.keys(), "id")
