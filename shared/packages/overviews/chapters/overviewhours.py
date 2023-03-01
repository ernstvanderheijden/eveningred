from ..fragments.overviewhoursgrid import Overviewhoursgrid
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

fragmentname1 = "overviewhoursgrid"


class Overviewhours(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        # self.context = add_variables(request)
        self.level = request.GET.get('level', 0)
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Overviewhoursgrid(request, pk))).render_fragment_grid(),
                    "width": 12,
                }
            }
        ]
