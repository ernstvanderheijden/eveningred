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
                {
                    "Detail": {
                        "name_active_chapter": "detail",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
                    },
                },
                {
                    "Relaties": {
                        "name_active_chapter": "relations",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=relations&pk=" + str(pk),
                    },
                },
            ]
        else:
            self.chaptermenu = []
