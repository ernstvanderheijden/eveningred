from shared.functions import get_crud_contenttitle


class Crud:
    def __init__(self, request, viewtype, pk=None):
        super().__init__()
        self.pk = pk
        self.viewtype = viewtype
        self.contenttitle = get_crud_contenttitle(viewtype)
        self.record = ''

        self.level = request.GET.get('level', 0)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.order_by = "description"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        if viewtype == 'create':
            self.footer_button_html = "core/actions/save.html"
        elif viewtype == 'delete':
            self.modalsize = "modalsm"
            self.templatename = 'core/delete/confirm_delete.html'
        else:
            self.footer_button_html = "core/actions/save_delete.html"
