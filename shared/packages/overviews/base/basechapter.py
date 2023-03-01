from .basepackage import Basepackage


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Overzichten"
        # self.leftsubmenuactive = "Urenoverzicht"
        self.contenttitle = 'Urenoverzicht'

        if pk:
            self.chaptermenu = [
            ]
        else:
            self.chaptermenu = [
                {
                    "Urenoverzicht": {
                        "name_active_chapter": "overviewhours",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=overviewhours",
                    },
                },
                {
                    "Materiaaloverzicht": {
                        "name_active_chapter": "overviewmaterials",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=overviewmaterials",
                    },
                },
            ]
