from users.models import User
from shared.functions import get_crud_contenttitle

modelname = "User"


class Crudchangepassword:
    def __init__(self, request, viewtype, pk=None):
        pk = request.user.id
        self.pk = pk
        self.viewtype = viewtype
        self.contenttitle = get_crud_contenttitle(viewtype)

        self.level = request.GET.get('level', 0)
        self.modelname = modelname
        self.record = ''
        self.record = User.objects.get(id=pk)
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.order_by = "first_name"
        self.successurl = request.GET.get('successurl', '')
        self.templatename = 'core/forms/form.html'
        self.fragment = request.GET.get('fragment', '')
        self.modalsize = "modalmd"
        self.deny_del_or_upd = User.dependencies(pk)

        self.footer_button_html = "core/actions/save.html"

        self.messagelist = ["Het wachtwoord is gewijzigd", "success"]  # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
