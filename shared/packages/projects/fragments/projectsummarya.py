from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from projects.models import Project


class ProjectsummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "description": {"caption": "Omschrijving", "fieldtype": "char", },
            "relationid__relationname": {"caption": "Relatie", "fieldtype": "char", },
            "startdate": {"caption": "Startdatum", "fieldtype": "date", },
        }
        records = Project.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
