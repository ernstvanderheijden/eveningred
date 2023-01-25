from relations.models import Relation
from shared.packages.estates.base.baseform import Baseform

packagename = 'estates'
modelname = "Estate"
fk_modelname = "Relation"


class Estateform(Baseform):
    def __init__(self, request=None):
        super().__init__(request)

        relationid = request.GET.get('fk', 0)
        if relationid:
            relationname = Relation.objects.get(id=int(relationid)).relationname
            self.ownerid.update({
                "caption": "Relatie",
                "modal_select": True,
                "initial": relationid,
                "showvalue": relationname,
                "onclick": "",
                "blocked_when_used": True,
            })
