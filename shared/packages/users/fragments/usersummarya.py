from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from users.models import User


class UsersummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "first_name": {
                "caption": "Voornaam",
                "fieldtype": "char",
            },
            "last_name": {
                "caption": "Achternaam",
                "fieldtype": "number",
            },
            "email": {
                "caption": "E-mail",
                "fieldtype": "char",
            },
            "relationid__relationname": {
                "caption": "Relatie",
                "fieldtype": "char",
            },
        }
        self.record = User.objects.filter(id=pk).values(*self.columnfields.keys(), 'id',)[0]
