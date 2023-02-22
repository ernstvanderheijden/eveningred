from ..base.baseform import Baseform

modelname = "Material"


class Materialform(Baseform):
    def __init__(self, request):
        super().__init__(request)
