from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from users.models import User


class UsersummaryB(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "username": {
                "caption": "Inlognaam",
                "fieldtype": "char",
            },
            "status": {
                "caption": "Status",
                "fieldtype": "status_choice",
            },
            "is_employee": {
                "caption": "Medewerker",
                "fieldtype": "boolean",
            },
            "is_employee_read": {
                "caption": "Medewerker leesrechten",
                "fieldtype": "boolean",
            },
            "is_employee_write": {
                "caption": "Medewerker schrijfrechten",
                "fieldtype": "boolean",
            },
            "is_manager": {
                "caption": "Manager",
                "fieldtype": "boolean",
            },
        }
        self.record = User.objects.filter(id=pk).values(*self.columnfields.keys(), 'id',)[0]
