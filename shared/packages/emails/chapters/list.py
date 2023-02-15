from ..fragments.emaillist import Emaillist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Email"
fragmentname1 = "emaillist"


class List(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        # self.context = add_variables(request)
        self.level = request.GET.get('level', 0)
        self.tools = {}
        self.fragments = [
            {
                fragmentname1: {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Emaillist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
