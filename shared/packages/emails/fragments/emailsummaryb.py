from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from emails.models import Email


class Emailsummaryb(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.level = request.GET.get('level', 0)
        # self.fragmenttype = "summary"
        self.render_templates = {
            "refreshtarget": "fragment",
            "summary_inner_html": "core/fragments/summary/summary_inner.html",
            "summary_html": "core/fragments/summary/summary.html",
        }

        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "attachments": {"caption": "Bijlagen", "fieldtype": "pill_list", },
            "createdate": {"caption": "Aanmaakdatum", "fieldtype": "datetime", },
            "creatorid__first_name": {"caption": "Aangemaakt door", "fieldtype": "char"},
            # "updatedate": {"caption": "Bijwerkdatum", "fieldtype": "datetime", },
            # "updaterid__first_name": {"caption": "Bijgewerkt door", "fieldtype": "char"},
        }
        records = Email.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
