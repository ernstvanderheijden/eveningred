from master.models import Articlegroup, Vattype, Unittype

modelname = "Article"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.description = {
            "autofocus": "autofocus",
            "class": "",
            "label": "Omschrijving",
        }
        self.price = {
            "label": "Prijs excl. BTW",
        }
        self.unittypeid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Eenheid",
            "choicelist": [('', '---')] + [(c.id, str(c.description)) for c in Unittype.objects.filter(status=0).order_by("description")],
        }
        self.articlegroupid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Artikelgroep",
            "choicelist": [('', '---')] + [(c.id, str(c.description)) for c in Articlegroup.objects.filter(status=0).order_by("description")],
        }
        self.vattypeid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "BTW type",
            "choicelist": [('', '---')] + [(c.id, str(c.description)) for c in Vattype.objects.filter(status=0).order_by("description")],
        }
