from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from materials.models import Material


class MaterialsummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "customerid__relationname": {"caption": "Leverancier", "fieldtype": "char", },
            "projectid__description": {"caption": "Project", "fieldtype": "char", },
            "issuedate": {"caption": "Uitgiftedatum", "fieldtype": "date", },
            "description": {"caption": "Omschrijving", "fieldtype": "char", },
            "purchasingcosts": {"caption": "Bedrag", "fieldtype": "decimal", },
            "userid__fullname": {"caption": "Gebruiker", "fieldtype": "char", },
        }
        records = Material.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
