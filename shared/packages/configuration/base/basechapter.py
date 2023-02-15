from .basepackage import Basepackage
from configuration.models import Configuration


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Instellingen"
        self.deny_del_or_upd = Configuration.dependencies(pk)

        if pk:
            self.contenttitle = "Instellingen"
            self.chaptermenu = []
        else:
            self.chaptermenu = []
