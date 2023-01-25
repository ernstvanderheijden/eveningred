from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from applog.models import Applog


class Applogsummarya(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        # self.fragmenttype = "summary"
        self.render_templates = {
            "refreshtarget": "fragment",
            "summary_inner_html": "core/fragments/summary/summary_inner.html",
            "summary_html": "core/fragments/summary/summary.html",
        }

        self.columnfields = {  # Fieldtypes are: boolean, char, date, applog, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "id": {"caption": "Id", "fieldtype": "number"},
            "created": {"caption": "Datum", "fieldtype": "datetime", },
            "app_name": {"caption": "App", "fieldtype": "char", },
            "model_name": {"caption": "Tabel", "fieldtype": "char", },
            "model_id": {"caption": "Tabelid", "fieldtype": "char", },
            "reason": {"caption": "Reden", "fieldtype": "char", },
            "messagetype": {"caption": "Berichttype", "fieldtype": "char", },
            "message": {"caption": "Bericht", "fieldtype": "char", },
            "severity": {"caption": "Impact", "fieldtype": "severity_choice", },
        }
        self.record = Applog.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')[0]
