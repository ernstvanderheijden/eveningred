from .basepackage import Basepackage


class Basechapter(Basepackage):
    def __init__(self, request, pk):
        super().__init__()
        self.leftmenuactive = "Dashboard"
        # self.leftsubmenuactive = "Dashboard"
        self.deny_del_or_upd = False

        self.chaptermenu = []
