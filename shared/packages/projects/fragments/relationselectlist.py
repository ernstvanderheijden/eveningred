from shared.packages.relations.base.baseselectlist import BaseSelectList

packagename = 'projects'
fieldname_select = 'relationid'


class Relationselectlist(BaseSelectList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request, viewtype, pk=None)
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        # self.modalsize = 'modalxl'
        self.onclick = "set_clicked_value_to_previous_modal(" + str(self.level) + ", '" + fieldname_select + "', 'pk_replace', 'displayfield_replace')"
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
