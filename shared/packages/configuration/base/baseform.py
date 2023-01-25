from master.models import Paymenttype, Conditiontype

modelname = "Configuration"
packagename = "configuration"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.is_default = {
            "label": "Standaard",
        }
        self.days_in_front = {
            "label": "Planbord aantal dagen ervoor",
            "fieldtype": "number",
        }
        self.on_each_side = {
            "label": "Paginering, aantal beide zijden",
            "fieldtype": "number",
        }
        self.on_ends = {
            "label": "Paginering, aantal aan eind",
            "fieldtype": "number",
        }
        self.conditions = {
            "label": "Link naar Voorwaarden",
        }
        self.regulations = {
            "label": "Link naar Voorschriften",
        }
        self.conditiontypeid = {
            "label": "Standaard betalingstermijn",
            "choicelist": [(c.id, str(c.description)) for c in Conditiontype.objects.filter(status=0).order_by("description")],
        }
        self.paymenttypeid = {
            "label": "Standaard betaalwijze",
            "choicelist": [(c.id, str(c.description)) for c in Paymenttype.objects.filter(status=0).order_by("description")],
        }
        self.email_to_accountancy = {
            "label": "Accountancy e-mailadres",
        }
        self.email_display_name = {
            "label": "Afzender naam",
        }
        self.email_from = {
            "label": "Afzender e-mailadres",
        }
        self.email_reply_to = {
            "label": "Afzender antwoordadres",
        }
        self.email_logo = {
            "label": "Link naar e-mail logo",
        }
        self.homepage = {
            "label": "Link naar home pagina",
        }
        self.aboutuspage = {
            "label": "Link naar over-ons pagina",
        }
        self.contactpage = {
            "label": "Link naar contact pagina",
        }
        self.instagrampage = {
            "label": "Link naar instagram pagina",
        }
        self.facebookpage = {
            "label": "Link naar facebook pagina",
        }
