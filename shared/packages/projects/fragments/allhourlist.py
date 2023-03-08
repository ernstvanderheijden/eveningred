from core.globals.global_fragments import GlobalList
from core.globals.global_functions import encode_string
from hours.models import Hour

nameform = 'hourform'
crudname = 'crud'


class Allhourlist(GlobalList):
    def __init__(self, request, viewtype, pk=None):
        super().__init__(request)
        self.contenttitle = 'Alle urenregistraties'
        self.fragment = __class__.__name__.lower()
        self.fragmentrefresh = __class__.__name__.lower()
        self.clickevent = 'selectmultiple'  # Action @ click on row (detail, update, selectsingle, selectmultiple)
        self.order_by = "-issuedate"
        self.paginatesize_overwrite = ''
        self.successurl_decoded = "/core/fragment/?level=" + self.level + "&package=" + self.package + "&fragment=" + self.fragment + "&pk=" + str(self.pk) + "&fragmentrefresh=data_" + self.fragment + "&refreshtarget=data&page=1"
        self.onclick = "do_url('" + self.fragment + "', " + str(int(self.level) + 1) + ", '/core/update/pk_replace/?level=" + str(int(self.level) + 1) + "&package=hours&crud=" + crudname + \
                       "&fk=&pk=pk_replace&nameform=" + nameform + "&successurl=" + encode_string(self.successurl_decoded) + "')"
        if request.user.has_perm('projects.process_project'):
            self.tools.update({
                'execute_download_xlsx': {
                    "id": str(self.level) + "_" + self.fragment + "_process_selected_records",
                    "title": "Downloaden",
                    "tooltype": "button_href",
                    "class": "btn btn-primary",
                    "url": "/shared/execute_download_xlsx/?level=0&package=hours",
                    "disabled": True,
                    # "disabled_explanation": "Geen regels geselecteerd",
                },
            })
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "issuedate": {
                "caption": "Datum",
                "fieldtype": "date",
                "operator": "__icontains",
            },
            "amounthours": {
                "caption": "Aantal",
                "fieldtype": "decimal",
                "operator": "__icontains",
            },
            "description": {
                "caption": "Omschrijving",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "projectid__description": {
                "caption": "Project",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "userid__fullname": {
                "caption": "Gebruiker",
                "fieldtype": "char",
                "operator": "__icontains",
            },
            "processdate": {
                "caption": "Verwerkdatum",
                "fieldtype": "date",
                "operator": "__icontains",
            },
        }
        self.records = Hour.objects.filter().values(*self.columnfields.keys(), "id")
        self.render_templates.update({
            "list_inner_data_html": "shared/list/download_list_inner_data.html",
        })
