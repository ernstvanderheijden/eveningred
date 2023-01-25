from master.models import Vattype
from .crud import Crud

modelname = "Vattype"
nameform = "vattypeform"


class Crudvattype(Crud):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.crud = __class__.__name__.lower()
        self.modelname = modelname
        if pk:
            self.record = Vattype.objects.get(id=pk)
        self.nameform = nameform
        self.deny_del_or_upd = Vattype.dependencies(pk)
