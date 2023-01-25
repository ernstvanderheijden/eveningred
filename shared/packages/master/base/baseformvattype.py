modelname = "Vattype"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self):
        super().__init__()
        self.description = {
                'autofocus': 'autofocus',
                "class": "",
                "label": "Omschrijving",
                "required": True,
                "blocked_when_used": True,
            }
        self.percentage = {
            "label": "Percentage",
        }
        self.vatcode = {
            "label": "BTW code",
        }
        # self.status = {
        #     "label": "Status",
        # }
