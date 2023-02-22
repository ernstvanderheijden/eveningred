from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from hours.models import Hour


class HoursummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "projectid__description": {"caption": "Project", "fieldtype": "char", },
            "issuedate": {"caption": "Datum", "fieldtype": "date", },
            "description": {"caption": "Omschrijving", "fieldtype": "char", },
            "amounthours": {"caption": "Aantal", "fieldtype": "decimal", },
            "userid__fullname": {"caption": "Gebruiker", "fieldtype": "number", },
        }
        records = Hour.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
