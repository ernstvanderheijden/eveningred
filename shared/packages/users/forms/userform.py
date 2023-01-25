from ..base.baseform import Baseform

modelname = "User"


class Userform(Baseform):
    def __init__(self, request):
        super().__init__(request)
