from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from articles.models import Article


class ArticlesummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "description": {"caption": "Artikel", "fieldtype": "char", },
            "price": {"caption": "Prijs excl. BTW", "fieldtype": "number", },
            "unittypeid__description": {"caption": "Eenheid", "fieldtype": "char", },
            "articlegroupid__description": {"caption": "Artikelgroep", "fieldtype": "char", },
            "vattypeid__description": {"caption": "BTW type", "fieldtype": "char", },
        }
        records = Article.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
