from master.models import Paymenttype
from .crud import Crud

modelname = "Paymenttype"
nameform = "paymenttypeform"


class Crudpaymenttype(Crud):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.crud = __class__.__name__.lower()
        self.modelname = modelname
        if pk:
            self.record = Paymenttype.objects.get(id=pk)
        self.nameform = nameform
        self.deny_del_or_upd = Paymenttype.dependencies(pk)
