from .basepackage import Basepackage
from relations.models import Relation


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Relatiebeheer"
        # self.leftsubmenuactive = "Relaties"
        self.deny_del_or_upd = Relation.dependencies(pk)

        if pk:
            self.contenttitle = Relation.objects.get(id=pk).relationname
            self.chaptermenu = [
                # {
                #     "Detail": {
                #         "name_active_chapter": "detail",
                #         "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
                #     },
                # },
            ]
        else:
            self.chaptermenu = []
