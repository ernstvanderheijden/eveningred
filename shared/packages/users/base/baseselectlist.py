from core.globals.global_fragments import GlobalList
from users.models import User


class BaseSelectList(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = "Gebruikers"
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "username"
        self.paginatesize_overwrite = ''
        self.displayfield = 'username'
        self.disable_onclick_after_click = True
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "username": {
                "caption": "Gebruiker",
                "fieldtype": "char",
                "operator": "__icontains",
            },

        }
        self.records = User.objects.filter(status=0).values(*self.columnfields.keys(), "id", "status")
        self.html_header = "core/modals/modalheader.html"
        self.html_footer = "core/modals/modalfooter.html"
