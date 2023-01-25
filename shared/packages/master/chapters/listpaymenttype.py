from ..fragments.paymenttypelist import Paymenttypelist
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Paymenttype"
fragmentname1 = "paymenttypelist"


class Listpaymenttype(Basechapter):
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
                    "rendered_string": RenderCtxAndContext(request, vars(Paymenttypelist(request, pk))).render_fragment_list(),
                    "width": 12,
                }
            }
        ]
