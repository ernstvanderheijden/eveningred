from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from emails.models import Email


class Emailsummarya(Basepackage, GlobalSummary):
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

        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            # "id": {"caption": "Id", "fieldtype": "number"},
            "to_email": {"caption": "Aan", "fieldtype": "pill_list", },
            "cc_email": {"caption": "CC", "fieldtype": "pill_list", },
            "bcc_email": {"caption": "BCC", "fieldtype": "pill_list", },
            "from_email": {"caption": "Van", "fieldtype": "char", },
            "reply_to": {"caption": "Antwoord naar", "fieldtype": "char", },
            "mail_subject": {"caption": "Onderwerp", "fieldtype": "char", },
        }
        records = Email.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
