from .basepackage import Basepackage
from users.models import User


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Gebruikersbeheer"
        # self.leftsubmenuactive = "Gebruikers"
        self.deny_del_or_upd = User.dependencies(pk)

        if pk:
            self.contenttitle = User.objects.get(id=pk).fullname
            self.chaptermenu = []
        else:
            self.chaptermenu = []
