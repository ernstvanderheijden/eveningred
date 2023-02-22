import datetime

from projects.models import Project
from users.models import User

modelname = "Hour"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.userid = {
            "hidden": True,
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Gebruiker",
            "choicelist": [(c.id, str(c.fullname)) for c in User.objects.filter(status=0, id=request.user.id).order_by("fullname")],
            "initial": request.user.id,
        }
        self.projectid = {
            "class": "",
            "fieldtype": 'dropdown',
            "label": "Project",
            "choicelist": [('', '---')] + [(c.id, str(c.description)) for c in Project.objects.filter(status=0).order_by("description")],
        }
        self.issuedate = {
            "class": "",
            "label": "Datum",
            "datepicker": True,
            "initial": datetime.datetime.today().date,
        }
        self.description = {
            # "autofocus": "autofocus",
            "class": "",
            "label": "Omschrijving",
        }
        self.amounthours = {
            "label": "Uren gewerkt",
        }
