from ..fragments.emailsummarya import Emailsummarya
from ..fragments.emailsummaryb import Emailsummaryb
from ..fragments.emailsummaryc import Emailsummaryc
from ..fragments.emailsummaryd import Emailsummaryd
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext

modelname = "Email"
nameform = "emailform"
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
                "emailsummarya": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Emailsummarya(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
                "emailsummaryb": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Emailsummaryb(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
                "emailsummaryc": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Emailsummaryc(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
                "emailsummaryd": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Emailsummaryd(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
