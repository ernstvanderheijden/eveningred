from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from configuration.models import Configuration


class Configurationsummarya(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = "Weergave"
        self.level = request.GET.get('level', 0)

        # self.fragmenttype = "summary"
        self.render_templates = {
            "refreshtarget": "fragment",
            "summary_inner_html": "core/fragments/summary/summary_inner.html",
            "summary_html": "core/fragments/summary/summary.html",
        }

        self.columnfields = {  # Fieldtypes are: boolean, char, date, applog, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "days_in_front": {
                "caption": "Planbord, aantal dagen ervoor",
                "fieldtype": "number"
            },
            "on_each_side": {
                "caption": "Paginering, aantal beide zijden",
                "fieldtype": "number"
            },
            "on_ends": {
                "caption": "Paginering, aantal aan eind",
                "fieldtype": "number"
            },
        }

        self.record = Configuration.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')[0]
