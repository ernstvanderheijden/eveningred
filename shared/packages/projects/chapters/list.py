from ..fragments.projectlist import Projectlist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Project"
fragmentname1 = "projectlist"


class List(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee_read", "write": "is_employee_write"}, {"read": "is_manager", "write": "is_manager"}]
        self.tools = {
        }
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Projectlist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
