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
        self.status = {
            "label": "Status",
            "required": True,
        }
