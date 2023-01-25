from projects.models import Project
from ..fragments.projectsummarya import ProjectsummaryA
from ..fragments.projectsummaryb import ProjectsummaryB
from ..base.basechapter import Basechapter
from core.functions.render_fragments import RenderCtxAndContext
from core.globals.global_functions import encode_string

modelname = "Project"
nameform = "projectform"
return_to_detail = "detail"
return_to_list = "list"
fragmentname1 = "projectsummarya"
fragmentname2 = "projectsummaryb"


class Detail(Basechapter):
    def __init__(self, request, viewtype=None, pk=None):
        super().__init__(request, pk)
        self.pk = pk
        self.viewtype = viewtype
        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee_read", "write": "is_employee_write"}, {"read": "is_manager", "write": "is_manager"}]

        self.tools = {
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
        }
        # record = Project.objects.get(id=self.pk)
        # if record.is_master:
        #     self.tools['delete'].update({
        #         "url": "",
        #         "disabled": True,
        #     })

        self.fragments = [
            {
                fragmentname1: {
                    "rendered_string": RenderCtxAndContext(request, vars(ProjectsummaryA(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
            {
                fragmentname2: {
                    "rendered_string": RenderCtxAndContext(request, vars(ProjectsummaryB(request, self.pk))).render_fragment_summary(),
                    "width": 6,
                },
            },
        ]
