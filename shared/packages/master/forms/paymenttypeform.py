from ..base.baseformpaymenttype import Baseform

modelname = "Paymenttype"


class Paymenttypeform(Baseform):
    def __init__(self, request):
        super().__init__()
