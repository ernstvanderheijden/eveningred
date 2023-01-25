from core.globals.global_fragments import GlobalSummary
from ..base.basepackage import Basepackage
from relations.models import Relation


class RelationsummaryA(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.rights_crud = [{"read": "is_employee", "write": "is_employee"}, {"read": "is_manager", "write": "is_manager"}]
        self.columnfields = {  # Fieldtypes are: boolean, boolean_true, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pill_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "relationname": {"caption": "Relatienaam", "fieldtype": "char", },
            "firstname": {"caption": "Voornaam", "fieldtype": "char", },
            "lastname": {"caption": "Achternaam", "fieldtype": "char", },
            "fulladdress": {"caption": "Adres", "fieldtype": "char", },
            "phone": {"caption": "Telefoon", "fieldtype": "telephone", },
            "email": {"caption": "E-mail", "fieldtype": "link", },
            "dateofbirth": {"caption": "Geboortedatum", "fieldtype": "date", },
            "placeofbirth": {"caption": "Geboorteplaats", "fieldtype": "char", },
            "licenseplate": {"caption": "Kenteken", "fieldtype": "licenseplate", },
        }
        records = Relation.objects.filter(id=pk).values(*self.columnfields.keys(), 'id')
        for record in records:
            self.record = record
