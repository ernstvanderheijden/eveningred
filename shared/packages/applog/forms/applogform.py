from ..base.baseform import Baseform

modelname = "Applog"
packagename = "applog"


class Applogform(Baseform):
    def __init__(self, request):
        super().__init__(request)
