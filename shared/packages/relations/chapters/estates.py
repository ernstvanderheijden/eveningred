from ..fragments.estatelist import Estatelist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Estate"
fragmentname1 = "estatelist"


class Estates(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.pk = pk
        self.viewtype = viewtype
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(Estatelist(request, self.viewtype, self.pk))).render_fragment_list(),
                    "width": 12,
                },
            },
        ]
