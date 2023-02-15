from core.globals.global_fragments import GlobalList
from relations.models import Relation


class BaseSelectList(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = "Relaties"
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "relationname"
        self.modalsize = "modalxl"
        self.paginatesize_overwrite = ''
        self.displayfield = 'relationname'
        self.disable_onclick_after_click = True
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
            "city": {
                "caption": "Plaats",
                "fieldtype": "char",
                "operator": "__icontains",
            },
        }
        self.html_header = "core/modals/modalheader.html"
        self.records = Relation.objects.filter(status=0).values(*self.columnfields.keys(), "id", "status")
