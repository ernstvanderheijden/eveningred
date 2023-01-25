modelname = "Relation"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self, request):
        super().__init__()
        self.relationname = {
            "autofocus": "autofocus",
            "class": "",
            "label": "Relatienaam",
        }
        self.firstname = {
            "class": "",
            "label": "Voornaam",
        }
        self.lastname = {
            "class": "",
            "label": "Achternaam",
            # "required": True,
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
        self.phone = {
            "label": "Telefoon",
        }
        self.email = {
            "label": "E-mail",
        }
        # self.is_debtor = {
        #     "label": "Debiteur",
        # }
        # self.is_creditor = {
        #     "label": "Crediteur",
        # }
        # self.debtornr = {
        #     "label": "Debiteurnummer",
        # }
        # self.creditornr = {
        #     "label": "Crediteurnummer",
        # }
        # self.cocnr = {
        #     "label": "KvK nummer",
        # }
        # self.vatnr = {
        #     "label": "BTW nummer",
        # }
        # self.dateofbirth = {
        #     "label": "Geboortedatum",
        #     "datepicker": True,
        # }
        # self.placeofbirth = {
        #     "label": "Geboorteplaats",
        # }
        # self.licenseplate = {
        #     "label": "Kenteken",
        # }
        self.conditiontypeid = {
            "label": "Betalingstermijn",
            # "required": True,
        }
        self.paymenttypeid = {
            "label": "Betaalwijze",
            # "required": True,
        }
        self.sendmethod = {
            "label": "Verzendmethode",
            # See model Relation for e-mailaddress required. Is now grayed out
        }
        self.status = {
            "label": "Status",
        }
