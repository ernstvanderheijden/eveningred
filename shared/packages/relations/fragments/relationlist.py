from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from relations.models import Relation

nameform = 'relationform'


class Relationlist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "relationname"
        self.paginatesize_overwrite = ''
        self.displayfield = 'relationname'
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        if request.user.has_perm('relations.add_relation'):
            self.tools.update({
                'create': {
                    "title": "fas fa-plus",
                    "tooltype": "create",
                    "class": "btn btn-primary",
                    "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
                },
            })
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "relationname": {
                "caption": "Relatienaam",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "firstname": {
                "caption": "Voornaam",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "lastname": {
                "caption": "Achternaam",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "phone": {
                "caption": "Telefoon",
                "fieldtype": "phone",
                "operator": "__icontains",
            },
            "email": {
                "caption": "E-mail",
                "fieldtype": "link",
                "operator": "__icontains",
            },
            "licenseplate": {
                "caption": "Kenteken",
                "fieldtype": "licenseplate",
                "operator": "__icontains",
            },
        }
        self.records = Relation.objects.filter().values(*self.columnfields.keys(), "id", "status")
