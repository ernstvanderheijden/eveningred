from ..base.baseform import Baseform

modelname = "Article"


class Articleform(Baseform):
    def __init__(self, request):
        super().__init__(request)
