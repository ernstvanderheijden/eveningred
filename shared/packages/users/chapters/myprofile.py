from ..fragments.usersummarya import UsersummaryA
from ..fragments.usersummaryb import UsersummaryB
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext
from core.globals.global_functions import encode_string

modelname = "User"
nameform = "userprofileform"
return_to_detail = "myprofile"
return_to_list = "list"
fragmentname1 = "usersummarya"
fragmentname2 = "usersummaryb"


class Myprofile(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        self.pk = request.user.id
        super().__init__(request, self.pk)
        self.viewtype = viewtype
        self.level = request.GET.get('level', 0)
        self.contenttitle = "Mijn profiel"

        self.tools = {
            "set_password": {
                "title": "Wijzig wachtwoord",
                "tooltype": "button",
                "class": "btn btn-primary",
                "url": "/core/update/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crudchangepassword&nameform=" + nameform + "&passwordform=true&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
            },
            "update": {
                "title": "fas fa-pen",
                "tooltype": "update",
                "class": "btn btn-primary",
                "url": "/core/update/" + str(self.pk) + "?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
            },
        }

        # if not self.allow_update:
        #     self.tools['update'].update({"disabled": True, "url": ""})
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(UsersummaryA(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                fragmentname2: {
                    "rendered_string": RenderCtxAndContext(request, vars(UsersummaryB(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
