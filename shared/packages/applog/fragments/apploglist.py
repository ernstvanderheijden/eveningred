from core.globals.global_fragments import GlobalList
from applog.models import Applog

nameform = 'applogform'


class Apploglist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = ''
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'detail'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.onclick = "window.open('/core/template/?level=0&package=" + self.package + "&chapter=detail&pk=pk_replace', '_parent')"
        self.order_by = "-id"
        self.paginatesize_overwrite = ''
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.successurl_decoded = ""
        self.tools = {}
        self.columnfields = {  # Fieldtypes are: boolean, char, date, applog, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "id": {
                "caption": "ID",
                "fieldtype": "number",
                "operator": "__icontains",
            },
            "created": {
                "caption": "Datum",
                "fieldtype": "datetime",
                "operator": "__icontains",
            },
            "app_name": {
                "caption": "App",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "model_name": {
                "caption": "Tabel",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "model_id": {
                "caption": "Tabelid",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "reason": {
                "caption": "Reden",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "messagetype": {
                "caption": "Berichttype",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "message": {
                "caption": "Bericht",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "severity": {
                "caption": "Impact",
                "fieldtype": "severity_choice",
                "operator": "__icontains",
            },
        }
        self.records = Applog.objects.filter().values(*self.columnfields.keys(), "id")
