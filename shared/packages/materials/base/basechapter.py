from .basepackage import Basepackage
from materials.models import Material


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Mijn materiaalbeheer"
        # self.leftsubmenuactive = "Materialen"
        self.deny_del_or_upd = Material.dependencies(pk)

        if pk:
            self.contenttitle = Material.objects.get(id=pk).description
            self.chaptermenu = []
        else:
            self.chaptermenu = []
