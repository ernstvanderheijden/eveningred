from .basepackage import Basepackage
from hours.models import Hour


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Mijn urenbeheer"
        # self.leftsubmenuactive = "Uren"
        self.deny_del_or_upd = Hour.dependencies(pk)

        if pk:
            self.contenttitle = Hour.objects.get(id=pk).description
            self.chaptermenu = []
        else:
            self.chaptermenu = []
