modelname = "Articlegroup"


class Baseform:  # Baseform can not inherit from basepackage. Every declared variable becomes a field in the fieldlist (form)
    def __init__(self):
        super().__init__()
        # self.orderingid = {
        #         "class": "",
        #         "label": "Volgorde",
        #         "required": True,
        #         "blocked_when_used": False,
        #     }
        self.description = {
                'autofocus': 'autofocus',
                "class": "",
                "label": "Omschrijving",
                "required": True,
                "blocked_when_used": True,
            }
        # self.status = {
        #     "label": "Status",
        # }
