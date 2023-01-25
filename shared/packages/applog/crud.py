from applog.models import Applog
from shared.functions import get_crud_contenttitle

modelname = "Applog"


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
            self.record = Applog.objects.get(id=pk)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.order_by = "-id"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        self.deny_del_or_upd = Applog.dependencies(pk)
        if viewtype == 'delete':
            self.modalsize = "modalsm"
            self.footer_button_html = "core/actions/delete.html"
        else:
            self.footer_button_html = "core/actions/save.html"
