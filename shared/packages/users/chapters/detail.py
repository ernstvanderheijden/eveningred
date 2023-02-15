from ..fragments.usersummarya import UsersummaryA
from ..fragments.usersummaryb import UsersummaryB
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext
from core.globals.global_functions import encode_string

modelname = "User"
nameform = "userform"
return_to_detail = "detail"
return_to_list = "list"
fragmentname1 = "usersummarya"
fragmentname2 = "usersummaryb"


class Detail(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.pk = pk
        self.viewtype = viewtype
        self.level = request.GET.get('level', 0)
        self.tools = {}
        if request.user.has_perm('users.change_user'):
            self.tools.update({
                "usersendinvitation": {
                    "title": "fas fa-paper-plane",
                    "tooltype": "update",
                    "class": "btn btn-success",
                    "url": "/shared/action/actions/?level=" + str(int(self.level)) + "&pk=" + str(self.pk) + "&action=usersendinvitation&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
                },
                "update": {
                    "title": "fas fa-pen",
                    "tooltype": "update",
                    "class": "btn btn-primary",
                    "url": "/core/update/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
                }
            })
        if request.user.has_perm('users.delete_user'):
            self.tools.update({
                "delete": {
                    "title": "fas fa-trash-alt",
                    "tooltype": "delete",
                    "class": "btn btn-danger",
                    "url": "/core/delete/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_list)
                },
            })
            if int(self.pk) == request.user.id:
                self.tools['delete'].update({
                    "url": "",
                    "disabled": True,
                })

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
