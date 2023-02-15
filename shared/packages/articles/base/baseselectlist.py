from core.globals.global_fragments import GlobalList
from articles.models import Article


class BaseSelectList(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = "Artikelen"
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "description"
        self.paginatesize_overwrite = ''
        self.displayfield = 'description'
        self.disable_onclick_after_click = True
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "description": {
                "caption": "Artikel",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "unittypeid__unit": {
                "caption": "Eenheid",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "price": {
                "caption": "Prijs",
                "fieldtype": "currency",
                "operator": "__icontains",
            },

        }
        self.records = Article.objects.filter(status=0).values(*self.columnfields.keys(), "id", "status")
        self.html_header = "core/modals/modalheader.html"
        self.html_footer = "core/modals/modalfooter.html"
