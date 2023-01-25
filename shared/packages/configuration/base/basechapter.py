from .basepackage import Basepackage
from configuration.models import Configuration


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Instellingen"
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.deny_del_or_upd = Configuration.dependencies(pk)

        if pk:
            self.contenttitle = "Instellingen"
            self.chaptermenu = []
        else:
            self.chaptermenu = []
