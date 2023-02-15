from relations.models import Relation
from shared.functions import get_crud_contenttitle

modelname = "Relation"


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
            self.record = Relation.objects.get(id=pk)
        self.order_by = "relationname"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        self.deny_del_or_upd = Relation.dependencies(pk)
        if viewtype == 'delete':
            self.modalsize = "modalsm"
            self.templatename = 'core/delete/confirm_delete.html'
        else:
            self.footer_button_html = "core/actions/save.html"
            self.messagelist = ["Opgeslagen", "success", "short"]    # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
