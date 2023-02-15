from ..fragments.articlesummarya import ArticlesummaryA
from ..fragments.articlesummaryb import ArticlesummaryB
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext
from core.globals.global_functions import encode_string

modelname = "Article"
nameform = "articleform"
return_to_detail = "detail"
return_to_list = "list"
fragmentname1 = "articlesummarya"
fragmentname2 = "articlesummaryb"


class Detail(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.pk = pk
        self.viewtype = viewtype
        self.level = request.GET.get('level', 0)

        self.tools = {
            "update": {
                "title": "fas fa-pen",
                "tooltype": "update",
                "class": "btn btn-primary",
                "url": "/core/update/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
            },
            "delete": {
                "title": "fas fa-trash-alt",
                "tooltype": "delete",
                "class": "btn btn-danger",
                "url": "/core/delete/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_list)
            },
        }
        # if not self.allow_update:
        #     self.tools['update'].update({"disabled": True, "url": ""})
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(ArticlesummaryA(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                fragmentname2: {
                    "rendered_string": RenderCtxAndContext(request, vars(ArticlesummaryB(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
