from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from master.models import Articlegroup

nameform = 'articlegroupform'
crudname = 'crudarticlegroup'


class Articlegrouplist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = 'Artikelgroepen'
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "description"
        self.paginatesize_overwrite = ''
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.onclick = "do_url('" + self.fragment + "', " + str(int(self.level) + 1) + ", '/core/update/pk_replace/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=" + crudname + "&fk=&pk=pk_replace&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded) + "')"
        if request.user.has_perm('master.add_articlegroup'):
            self.tools.update({
                'create': {
                    "title": "fas fa-plus",
                    "tooltype": "create",
                    "class": "btn btn-success",
                    "url": "/core/create/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crudarticlegroup&fk=&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded)
                },
            })
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            # "orderingid": {
            #     "caption": "Volgorde",
            #     "fieldtype": "number",
            #     "operator": "__icontains",
            # },
            "description": {
                "caption": "Omschrijving",
                "fieldtype": "char",
                "operator": "__icontains",
            },
        }
        self.records = Articlegroup.objects.filter().values(*self.columnfields.keys(), "id")
