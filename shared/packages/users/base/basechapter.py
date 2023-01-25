from .basepackage import Basepackage
from users.models import User


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Gebruikersbeheer"
        # self.leftsubmenuactive = "Gebruikers"
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.deny_del_or_upd = User.dependencies(pk)

        if pk:
            self.contenttitle = User.objects.get(id=pk).fullname
            self.chaptermenu = []
        else:
            self.chaptermenu = []
