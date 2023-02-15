from .basepackage import Basepackage
from emails.models import Email


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Verzonden mail"
        # self.leftsubmenuactive = "Emails"
        self.deny_del_or_upd = Email.dependencies(pk)

        if pk:
            email = Email.objects.get(id=pk)
            self.contenttitle = "Email" + ' ' + str(email.id)
            # self.contenttitle = str(email.id) + " " + email.mail_subject
            # self.chaptermenu = [
            #     {
            #         "Detail": {
            #             "name_active_chapter": "detail",
            #             "chapterurl": "/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=" + str(pk),
            #         },
            #     },
            # ]
        # else:
        #     self.chaptermenu = []
#