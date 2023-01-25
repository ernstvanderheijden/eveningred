from master.models import Conditiontype
from .crud import Crud

modelname = "Conditiontype"
nameform = "conditiontypeform"


class Crudconditiontype(Crud):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.crud = __class__.__name__.lower()
        self.modelname = modelname
        if pk:
            self.record = Conditiontype.objects.get(id=pk)
        self.nameform = nameform
        self.deny_del_or_upd = Conditiontype.dependencies(pk)
