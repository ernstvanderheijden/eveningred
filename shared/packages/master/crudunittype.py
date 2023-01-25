from master.models import Unittype
from .crud import Crud

modelname = "Unittype"
nameform = "unittypeform"


class Crudunittype(Crud):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.crud = __class__.__name__.lower()
        self.modelname = modelname
        if pk:
            self.record = Unittype.objects.get(id=pk)
        self.nameform = nameform
        self.deny_del_or_upd = Unittype.dependencies(pk)
