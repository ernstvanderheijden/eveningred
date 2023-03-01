from core.globals.global_fragments import GlobalGrid
from hours.models import Hour
from shared.packages.overviews.functions import dict_hourgrid

# nameform = 'contactform'
# crudname = 'crudcontractform'


class Overviewhoursgrid(GlobalGrid):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = ""
        self.paginate = False
        self.hourgrid = dict_hourgrid(self)  # the scheduledata for estates
        self.records = {}
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&searchdate=" + format(self.searchdate, "%Y-%m-%d") + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.onclick = ""
        self.tools = {
        }
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice, choice_handlingtype
        }
