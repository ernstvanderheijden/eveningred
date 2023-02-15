# from core.globals.global_fragments import GlobalSummary
# from shared.contract import collect_contractlist_dashboard
# from shared.functions import list_to_string
# from ..base.basepackage import Basepackage
#
#
# class Checkcontracts(Basepackage, GlobalSummary):
#     def __init__(self, request, pk=None):
#         Basepackage.__init__(self)
#         GlobalSummary.__init__(self, request)
#         self.fragment = __class__.__name__.lower()
#         self.pk = pk
#         self.contenttitle = "Contractstatus"
#         self.level = request.GET.get('level', 0)
#         # self.fragmenttype = "summary"
#         self.render_templates = {
#             "refreshtarget": "fragment",
#             "summary_inner_html": "shared/summary/check_contracts.html",
#             "summary_html": "core/fragments/summary/summary.html",
#         }
#
#         # Collect data for check contracts
#         contractlist = collect_contractlist_dashboard()
#
#         self.fragmentdataset = {
#             "amount_contracts": {
#                 "caption": "Lopende contracten",
#                 "amount": len(contractlist['active_contracts']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts']) + "')"
#             },
#             "amount_contracts_concept": {
#                 "caption": "Concepten",
#                 "amount": len(contractlist['active_contracts_concept']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_concept']) + "')"
#             },
#             "amount_contracts_reservation": {
#                 "caption": "Wacht op bevestiging",
#                 "amount": len(contractlist['active_contracts_reservation']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_reservation']) + "')"
#             },
#             "amount_contracts_confirmed": {
#                 "caption": "Bevestigd",
#                 "amount": len(contractlist['active_contracts_confirmed']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_confirmed']) + "')"
#             },
#             "active_contracts_checkin_soon": {
#                 "caption": "Check-in binnen een week",
#                 "amount": len(contractlist['active_contracts_checkin_soon']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_checkin_soon']) + "')"
#             },
#             "amount_contracts_checkout": {
#                 "caption": "Uit te checken",
#                 "amount": len(contractlist['active_contracts_checkout']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_checkout']) + "')"
#             },
#             "amount_contracts_tofinish": {
#                 "caption": "Af te ronden",
#                 "amount": len(contractlist['active_contracts_tofinish']),
#                 "onclick": "do_url('dashboard', " + str(int(self.level) + 1) + ", '/core/fragment/?level=" + str(int(self.level) + 1) +
#                            "&package=contracts&fragment=contractselectlist&fk=&pk=&multiselect_records=" + list_to_string(contractlist['active_contracts_tofinish']) + "')"
#             },
#         }
