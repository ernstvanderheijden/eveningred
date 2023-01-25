from ..base.baseform import Baseform

modelname = "Email"
packagename = "emails"


class Emailform(Baseform):
    def __init__(self, request):
        super().__init__(request)
