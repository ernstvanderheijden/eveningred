modelname = "User"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.first_name = {
            "autofocus": "autofocus",
            "label": "Voornaam",
            "required": True,
        }
        self.last_name = {
            "label": "Achternaam",
            "required": True,
        }
        self.email = {
            "label": "E-mail",
            "required": True,
        }
        self.relationid = {
            "label": "Relatie",
            "required": False,
        }
        self.username = {
            "label": "Inlognaam",
            "required": True,
            "blocked_when_used": True,
        }
        self.is_employee = {
            "label": "Medewerker",
            "required": False,
        }
        self.is_employee_read = {
            "label": "Medewerker leesrechten",
            "required": False,
        }
        self.is_employee_write = {
            "label": "Medewerker schrijfrechten",
            "required": False,
        }
        self.is_manager = {
            "label": "Manager",
            "required": False,
        }
        self.status = {
            "label": "Status",
            "required": True,
        }
