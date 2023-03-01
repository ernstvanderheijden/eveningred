from configuration.models import Configuration
from core.globals.global_functions import date_range_dictionary
from datetime import datetime, timedelta


class GlobalList:
    def __init__(self, request):
        self.package = request.GET.get('package')
        self.fragment = request.GET.get('fragment', '')
        self.level = request.GET.get('level', 0)
        self.pk = request.GET.get('pk', '')
        self.page = request.GET.get('page', 1)
        self.paginate = True
        self.paginatesize_overwrite = ''
        self.tools = {}
        self.fragmenttype = "list"
        self.render_templates = {
            "refreshtarget": "fragment",
            "list_inner_data_html": "core/fragments/list/list_inner_data.html",
            "list_pagination_html": "core/fragments/list/list_pagination.html",
            "list_inner_html": "core/fragments/list/list_inner.html",
            "list_html": "core/fragments/list/list.html",
        }


class GlobalSummary:
    def __init__(self, request):
        self.level = request.GET.get('level', 0)
        self.pk = request.GET.get('pk', '')
        self.fragmenttype = "summary"
        self.successurl_decoded = ""
        self.render_templates = {
            "refreshtarget": "fragment",
            "summary_inner_html": "core/fragments/summary/summary_inner.html",
            "summary_html": "core/fragments/summary/summary.html",
        }


class GlobalGrid:
    def __init__(self, request):
        configuration = Configuration.default.get()
        self.package = request.GET.get('package')
        self.fragment = request.GET.get('fragment', '')
        self.level = request.GET.get('level', 0)
        self.pk = request.GET.get('pk', '')
        self.page = request.GET.get('page', 1)
        self.paginate = True
        self.tools = {}
        self.fragmenttype = "grid"

        self.today = datetime.today().date()
        self.weeks = request.GET.get('weeks', 2)
        self.days_in_front = configuration.days_in_front
        if request.GET.get('searchdate', ''):
            self.searchdate = datetime.strptime(request.GET.get('searchdate'), "%Y-%m-%d").date()
            weekday = self.searchdate.weekday()
            self.startdate = datetime.strptime(request.GET.get('searchdate'), "%Y-%m-%d").date() - timedelta(days=self.days_in_front + weekday)
        else:
            weekday = datetime.today().weekday()
            self.startdate = self.today - timedelta(days=self.days_in_front + weekday)
            self.searchdate = self.today
        self.enddate = self.searchdate + timedelta(days=(7 * self.weeks) - weekday - 1)
        self.columndates = date_range_dictionary(self.startdate, self.enddate)

        self.render_templates = {
            "refreshtarget": "fragment",
            "grid_inner_html": "shared/grid/overviewgrid_inner.html",
            "grid_html": "shared/grid/overviewgrid.html",
        }


# class GlobalInlineFomset:
#     def __init__(self, request):
#         self.viewtype = 'inlineformset'
#         self.level = request.GET.get('level', 0)
#         self.pk = request.GET.get('pk', '')
#         self.fragmenttype = "inlineformset"
#         self.successurl_decoded = ""
#         self.render_templates = {
#             "refreshtarget": "fragment",
#             "inlineformset_html": "core/forms/inlineformset.html",
#         }


# class GlobalAction:
#     def __init__(self, request):
#         self.level = request.GET.get('level', 0)
#         self.pk = request.GET.get('pk', '')
#         self.fragmenttype = "action"
#         self.order_by = ""
#         self.successurl_decoded = ""
#         self.render_templates = {
#             "refreshtarget": "fragment",
#             "action_html": "core/fragments/action/action.html",
#         }
#         self.contenttitle = "Actie"
#         self.fragment = __class__.__name__.lower()
#         self.fragmentrefresh = __class__.__name__.lower()
#         self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
#         self.donotclose = False  # This keeps the modal selectlist for creating a new record open
#
#         self.html_header = "core/modals/modalheader.html"
