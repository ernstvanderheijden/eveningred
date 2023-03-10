from .basepackage import Basepackage
from articles.models import Article


class Basechapter(Basepackage):
    def __init__(self, request, pk=None):
        super().__init__()
        self.leftmenuactive = "Artikelbeheer"
        # self.leftsubmenuactive = "Artikelen"
        self.deny_del_or_upd = Article.dependencies(pk)

        if pk:
            self.contenttitle = Article.objects.get(id=pk).description
            self.chaptermenu = []
        else:
            self.chaptermenu = []
