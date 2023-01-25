from projects.models import Project
from shared.functions import get_crud_contenttitle

modelname = "Project"


class Crud:
    def __init__(self, request, viewtype, pk=None):
        super().__init__()
        self.pk = pk
        self.viewtype = viewtype
        self.contenttitle = get_crud_contenttitle(viewtype)

        self.level = request.GET.get('level', 0)
        self.modelname = modelname
        self.record = ''
        if pk:
            self.record = Project.objects.get(id=pk)
        self.rights_crud = [{"read": "is_employee_read", "write": "is_employee_write"}, {"read": "is_manager", "write": "is_manager"}]
        self.order_by = "description"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        self.deny_del_or_upd = Project.dependencies(pk)
        if viewtype == 'delete':
            self.modalsize = "modalsm"
            self.templatename = 'core/delete/confirm_delete.html'
        else:
            self.footer_button_html = "core/actions/save.html"
            self.messagelist = ["Opgeslagen", "success", "short"]    # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
