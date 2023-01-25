from master.models import Articlegroup
from .crud import Crud

modelname = "Articlegroup"
nameform = "articlegroupform"


class Crudarticlegroup(Crud):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.crud = __class__.__name__.lower()
        self.modelname = modelname
        if pk:
            self.record = Articlegroup.objects.get(id=pk)
        self.nameform = nameform
        self.deny_del_or_upd = Articlegroup.dependencies(pk)
