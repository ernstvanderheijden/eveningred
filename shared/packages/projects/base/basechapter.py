from .basepackage import Basepackage
from projects.models import Project


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Projectbeheer"
        # self.leftsubmenuactive = "Projects"
        self.deny_del_or_upd = Project.dependencies(pk)

        if pk:
            self.contenttitle = Project.objects.get(id=pk).description
            self.chaptermenu = [
                # {
                #     "Detail": {
                #         "name_active_chapter": "detail",
                #         "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
                #     },
                # },
            ]
        else:
            if request.user.has_perm('projects.process_project'):
                self.chaptermenu = [
                    {
                        "Uren": {
                            "chapterbuttontype": "menuitem",
                            "names_active_button": ["listallhour", ],
                            "menuitems": [
                                {
                                    "caption": "Alle registraties",
                                    "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listallhour",
                                    "name_active_chapter": "allhour",
                                },
                            ],
                        },
                        "Materiaal": {
                            "chapterbuttontype": "menuitem",
                            "names_active_button": ["listallmaterial", ],
                            "menuitems": [
                                {
                                    "caption": "Alle uitgiftes",
                                    "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=listallmaterial",
                                    "name_active_chapter": "allmaterial",
                                },
                            ],
                        },
                    },
                ]
            else:
                self.chaptermenu = []
