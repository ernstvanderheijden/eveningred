from users.models import User
from shared.functions import get_crud_contenttitle

modelname = "User"


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
            self.record = User.objects.get(id=pk)
        self.order_by = "first_name"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        self.deny_del_or_upd = User.dependencies(pk)
        if viewtype == 'delete':
            self.modalsize = "modalsm"
            self.templatename = 'core/delete/confirm_delete.html'
        else:
            self.footer_button_html = "core/actions/save.html"
