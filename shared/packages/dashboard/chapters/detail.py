# from ..fragments.checkcontracts import Checkcontracts
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext
from ..fragments.empty import Empty

modelname = "Configuration"
return_to_detail = ""


class Detail(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.pk = pk
        self.viewtype = viewtype
        if request.GET.get('pk', ''):
            self.pk = request.GET.get('pk')
        self.level = request.GET.get('level', 0)

        self.tools = {}
        self.fragments = [
            {
                # "checkcontracts": {  # Don't forget to give this option the name of the list
                #     "rendered_string": RenderCtxAndContext(request, vars(Checkcontracts(request, self.pk))).render_fragment_summary(),
                #     "width": 6,
                # },
                "empty": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Empty(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
