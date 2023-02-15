from core.globals.global_fragments import GlobalList
from projects.models import Project


class BaseSelectList(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = "Projects"
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "description"
        self.modalsize = "modalxl"
        self.paginatesize_overwrite = ''
        self.displayfield = 'description'
        self.disable_onclick_after_click = True
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "description": {
                "caption": "Omschrijving",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "street": {
                "caption": "Straat",
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
        self.records = Project.objects.filter(status=0).values(*self.columnfields.keys(), "id", "status")
