from core.globals.global_fragments import GlobalList
from emails.models import Email

nameform = 'emailform'


class Emaillist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "-createdate"
        self.paginatesize_overwrite = ''
        self.successurl_decoded = ""
        self.tools = {}
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "createdate": {
                "caption": "Verzonden op",
                "fieldtype": "datetime",
                "operator": "__icontains",
            },
            "to_email": {
                "caption": "Aan",
                "fieldtype": "pill_list",
                "operator": "__icontains",
            },
            "cc_email": {
                "caption": "CC",
                "fieldtype": "pill_list",
                "operator": "__icontains",
            },
            "mail_subject": {
                "caption": "Onderwerp",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "status": {
                "caption": "Status",
                "fieldtype": "status_email",
                "operator": "__icontains",
            },
        }
        self.records = Email.objects.filter().values(*self.columnfields.keys(), "id")
