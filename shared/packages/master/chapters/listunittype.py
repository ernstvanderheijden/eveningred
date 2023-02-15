from ..fragments.unittypelist import Unittypelist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Unittype"
fragmentname1 = "unittypelist"


class Listunittype(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        # self.context = add_variables(request)
        self.level = request.GET.get('level', 0)
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Unittypelist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
