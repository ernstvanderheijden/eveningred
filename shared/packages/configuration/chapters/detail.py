from configuration.models import Configuration
from ..base.basechapter import Basechapter
from core.globals.global_functions import encode_string
from core.functions.render_fragments import RenderCtxAndContext
from ..fragments.configurationsummarya import Configurationsummarya
from ..fragments.configurationsummaryb import Configurationsummaryb
from ..fragments.configurationsummaryc import Configurationsummaryc
from ..fragments.configurationsummaryd import Configurationsummaryd
from ..fragments.configurationsummarye import Configurationsummarye
from ..fragments.configurationsummaryf import Configurationsummaryf

modelname = "Configuration"
nameform = "configurationform"
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

        self.tools = dict()
        self.record = Configuration.objects.get(id=self.pk)
        if self.record.is_default:
            self.tools.update({
                "default": {
                    "title": "Standaard",
                    "tooltype": "pill",
                    "class": "badge-success",
                },
            })

        self.tools.update({
            "update": {
                "title": "fas fa-pen",
                "tooltype": "update",
                "class": "btn btn-primary",
                "url": "/core/update/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_detail + "&pk=" + str(self.pk))
            },
            "delete": {
                "title": "fas fa-trash-alt",
                "tooltype": "delete",
                "class": "btn btn-danger",
                "url": "/core/delete/" + str(self.pk) + "/?level=" + str(int(self.level) + 1) + "&package=" + self.package + "&crud=crud&nameform=" + nameform + "&pk=" + str(self.pk) + "&successurl=" + encode_string("/core/template/?level=" + self.level + "&package=" + self.package + "&chapter=" + return_to_list)
            },
        })
        if self.record.is_default:
            self.tools.update({
                "delete": {
                    "title": "fas fa-trash-alt",
                    "tooltype": "delete",
                    "class": "btn btn-dark",
                    "url": "",
                    "disabled": True,
                },
            })

        self.fragments = [
            {
                "configurationsummarya": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummarya(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                "configurationsummaryb": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummaryb(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                "configurationsummaryc": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummaryc(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                "configurationsummaryd": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummaryd(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                "configurationsummaryc": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummarye(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                "configurationsummaryd": {  # Don't forget to give this option the name of the list
                    "rendered_string": RenderCtxAndContext(request, vars(Configurationsummaryf(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
