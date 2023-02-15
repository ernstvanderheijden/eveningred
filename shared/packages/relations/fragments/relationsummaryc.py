from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from relations.models import Relation


class RelationsummaryC(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "street": {"caption": "Straatnaam", "fieldtype": "char", },
            "number": {"caption": "Nummer", "fieldtype": "char", },
            "suffix": {"caption": "Toevoeging", "fieldtype": "char", },
            "postalcode": {"caption": "Postcode", "fieldtype": "char", },
            "city": {"caption": "Plaats", "fieldtype": "char", },
        }
        records = Relation.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
