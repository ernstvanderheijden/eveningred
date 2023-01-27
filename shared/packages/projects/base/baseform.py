modelname = "Project"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.description = {
            "autofocus": "autofocus",
            "class": "",
            "label": "Omschrijving",
        }
        self.relationid = {
            "label": "Relatie",
        }
        self.startdate = {
            "datepicker": True,
            "label": "Startdatum",
        }
        self.include = {
            "templatename": "core/actions/postcodenl.html",
        }
        self.street = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Straat",
        }
        self.number = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Nummer",
        }
        self.suffix = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Toevoeging",
        }
        self.postalcode = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Postcode",
        }
        self.city = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Plaats",
        }
        self.latitude = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Latitude",
        }
        self.longitude = {
            "included": True,  # Won't be shown, because part of the included
            "label": "Longitude",
        }
        self.status = {
            "label": "Status",
        }
