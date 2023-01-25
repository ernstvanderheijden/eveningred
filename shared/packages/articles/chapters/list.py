from ..fragments.articlelist import Articlelist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Article"
fragmentname1 = "articlelist"


class List(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Articlelist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
