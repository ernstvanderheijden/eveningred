from .basepackage import Basepackage
from relations.models import Relation


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Relatiebeheer"
        # self.leftsubmenuactive = "Relaties"
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.deny_del_or_upd = Relation.dependencies(pk)

        if pk:
            self.contenttitle = Relation.objects.get(id=pk).relationname
            self.chaptermenu = [
                {
                    "Detail": {
                        "name_active_chapter": "detail",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
                    },
                },
                {
                    "Objecten": {
                        "name_active_chapter": "estates",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=estates&pk=" + str(pk),
                    },
                },
            ]
        else:
            self.chaptermenu = []
