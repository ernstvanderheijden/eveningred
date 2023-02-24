from ..fragments.allmateriallist import Allmateriallist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Hour"
fragmentname1 = "allmateriallist"


class Listallmaterial(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        # self.context = add_variables(request)
        self.level = request.GET.get('level', 0)
        self.tools = {}

        if request.user.has_perm('projects.process_project'):
            self.fragments = [
                {
                    fragmentname1: {
                        "rendered_string": RenderCtxAndContext(request, vars(Allmateriallist(request, pk))).render_fragment_list(),
                        "width": 12,
                    }
                }
            ]
        else:
            self.fragments = []
