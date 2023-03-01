from django.db.models import Q

from ..base.basepackage import Basepackage
from core.globals.global_fragments import GlobalSummary
from django.contrib.auth.models import Permission, Group
from users.models import User


class UsersummaryB(Basepackage, GlobalSummary):
    def __init__(self, request, pk=None):
        Basepackage.__init__(self)
        GlobalSummary.__init__(self, request)
        self.fragment = __class__.__name__.lower()
        self.pk = pk
        self.contenttitle = ""
        self.columnfields = {  # Fieldtypes are: boolean, char, date, email, number, decimal, phone, sex, textarea, textarea_html, pil_list, editable_number, editable_dropdown, status_choice, status_contract, status_invoice
            "username": {
                "caption": "Inlognaam",
                "fieldtype": "char",
            },
            "status": {
                "caption": "Status",
                "fieldtype": "status_choice",
            },
        }
        self.record = User.objects.filter(id=pk).values(*self.columnfields.keys(), 'id',)[0]
        user = User.objects.get(id=pk)
        # Permissions examples

        # Set user_groups in a list
        self.usergroups = list()
        user_groups = user.groups.all()
        for user_group in user_groups:
            self.usergroups.append(user_group.id)

        self.groups = Group.objects.filter().exclude(name__startswith='X_').order_by('name')
        self.extra_template = "core/user/rights.html"

        permissions = Permission.objects.filter(Q(user=request.user) | Q(group__user=request.user)).all()
        for p in permissions:
            print("permissions", p, request.user)
        project_process = Group.objects.get(name='Projecten_verwerken')
        request.user.groups.add(project_process)  # Add the user to the Author group

        # if request.user.has_perm('projects.process_project'):
        #     print("PLOK process YES")
        # else:
        #     print("PLOK process NO")
