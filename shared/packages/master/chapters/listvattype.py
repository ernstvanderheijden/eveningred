from ..fragments.vattypelist import Vattypelist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Vattype"
fragmentname1 = "vattypelist"


class Listvattype(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        # self.context = add_variables(request)
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Vattypelist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
