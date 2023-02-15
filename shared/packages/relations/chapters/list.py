from ..fragments.relationlist import Relationlist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Relation"
fragmentname1 = "relationlist"


class List(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.level = request.GET.get('level', 0)
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Relationlist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
