from .basepackage import Basepackage


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Stamgegevens"
        # self.leftsubmenuactive = "Stamgegevens"
        self.contenttitle = 'Stamgegevens'

        self.chaptermenu = [
            {
                "Financiëel": {
                    "chapterbuttontype": "menuitem",
                    "names_active_button": ["listarticlegroup", "listunittype", "listvattype", "listconditiontype", "listpaymenttype", ],
                    "menuitems": [
                        {
                            "caption": "Artikelgroepen",
                            "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listarticlegroup",
                        },
                        {
                            "caption": "Eenheden",
                            "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listunittype",
                            "name_active_chapter": "unittype",
                        },
                        {
                            "caption": "BTW types",
                            "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listvattype",
                            "name_active_chapter": "vattype",
                        },
                        {
                            "caption": "Betalingstermijnen",
                            "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listconditiontype",
                        },
                        {
                            "caption": "Betaalmethoden",
                            "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listpaymenttype",
                            "name_active_chapter": "paymenttype",
                        },
                    ],
                },
            },
        ]
