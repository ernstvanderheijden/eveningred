from ..base.baseform import Baseform

modelname = "Configuration"
packagename = "configuration"


class Configurationform(Baseform):
    def __init__(self, request):
        super().__init__(request)
