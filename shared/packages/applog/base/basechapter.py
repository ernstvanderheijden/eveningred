from .basepackage import Basepackage
from applog.models import Applog


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Logboek"
        # self.leftsubmenuactive = "Applog"
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.deny_del_or_upd = Applog.dependencies(pk)

        if pk:
            applog = Applog.objects.get(id=pk)
            self.contenttitle = "Applog"
            # self.contenttitle = str(applog.id) + " " + applog.mail_subject
            self.chaptermenu = [
                {
                    "Detail": {
                        "name_active_chapter": "detail",
                        "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
                    },
                },
            ]
        else:
            self.chaptermenu = []
