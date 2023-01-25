from projects.models import Project
from relations.models import Relation
from ..base.baseform import Baseform

modelname = "Project"
packagename = "projects"


class Projectform(Baseform):
    def __init__(self, request):
        level = int(request.GET.get('level', 0)) + 1
        super().__init__(request)
        pk = request.GET.get('pk', '')
        relationname = ''
        initial = ''
        if pk:  # These next lines are to fill the dropdownfield(s) with the right data at update
            project = Project.objects.get(id=int(pk))
            # Foreign key Relation
            relation = Relation.objects.get(id=project.relationid_id)
            relationname = relation.relationname
            initial = relation.id
            deny_del_or_upd = Project.dependencies(pk)
            if deny_del_or_upd:
                pass

        self.relationid.update({
            "modal_select": True,
            "showvalue": relationname,
            "initial": initial,
            "onclick": "",
            "required": True,
        })
        self.relationid.update({
            "onclick": "do_url('', '" + str(level) + "', '/core/fragment/?level=" + str(level) + "&package=" + packagename +
                       "&fragment=relationselectlist&fragmentrefresh=body&refreshtarget=fragment&paginate=true&page=1')"
        })
