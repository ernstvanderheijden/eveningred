import datetime

from configuration.models import Configuration
from projects.models import Project
from relations.models import Relation
from users.models import User

modelname = "Material"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        configuration = Configuration.objects.get(is_default=True)
        self.userid = {
            "hidden": True,
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Gebruiker",
            "choicelist": [(c.id, str(c.fullname)) for c in User.objects.filter(status=0, id=request.user.id).order_by("fullname")],
            "initial": request.user.id,
        }
        self.customerid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Leverancier",
            "choicelist": [('', '---')] + [(c.id, str(c.relationname)) for c in Relation.objects.filter(status=0).order_by("relationname")],
            "initial": configuration.default_materials_customerid_id,
        }
        self.projectid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Project",
            "choicelist": [('', '---')] + [(c.id, str(c.description)) for c in Project.objects.filter(status=0).order_by("description")],
        }
        self.issuedate = {
            "class": "",
            "label": "Uitgiftedatum",
            "datepicker": True,
            "initial": datetime.datetime.today().date,
        }
        self.description = {
            # "autofocus": "autofocus",
            "class": "",
            "label": "Omschrijving",
        }
        self.purchasingcosts = {
            "label": "Bedrag",
        }
