from ..fragments.materiallist import Materiallist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Material"
fragmentname1 = "materiallist"


class List(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.level = request.GET.get('level', 0)
        self.tools = {}
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Materiallist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
