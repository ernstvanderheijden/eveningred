from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from estates.models import Estate

packagename = 'estates'
nameform = 'estateform'


class Estatelist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = 'Objecten'
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + packagename + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "description"
        self.paginatesize_overwrite = ''
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.tools = {
            'create': {
                "title": "fas fa-plus",
                "tooltype": "create",
                "class": "btn btn-primary",
                "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&fk=" + str(self.pk) + "&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
            },
        }
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "locationnumber": {
                "caption": "Standplaats",
                "fieldtype": "char",
                "operator": "__icontains",
            },
        }
        self.records = Estate.objects.filter(ownerid_id=self.pk).values(*self.columnfields.keys(), "id", "status")
