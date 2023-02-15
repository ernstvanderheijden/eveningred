from ..fragments.applogsummarya import Applogsummarya
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Applog"
nameform = "applogform"
return_to_detail = "detail"
return_to_list = "list"


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
                "applogsummarya": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Applogsummarya(request, self.pk))).render_fragment_summary(),
                    "width": 12,
                },
            },
        ]
