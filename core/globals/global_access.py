from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect

from core.globals.global_functions import is_ajax_request


class UserAccessMixin(PermissionRequiredMixin):
    permission_required = ''
    # raise_exception = False
    # permission_denied_message = "Geen rechten hiervoor"
    # login_url = '/'
    # redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        self.permission_required = set_required_rights(request, 'projects', 'projectform')
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            if is_ajax_request(request):
                data = dict()
                return JsonResponse(data)
            else:
                return redirect('/403/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

# http://klant1.eveningred.nl:8000/core/template/?level=0&package=projects&chapter=list


def set_required_rights(request, package, chapter):
    package = ''
    chapter = ''
    nameform = ''
    crudtype = ''

    if chapter == 'list' or chapter == 'detail':
        needed_right = 'read'

    if '/template/' in request.path:
        crudtype = 'template'
    elif '/create/' in request.path:
        crudtype = 'create'
    elif '/update/' in request.path:
        crudtype = 'update'
    if '/delete/' in request.path:
        crudtype = 'delete'

    print("PLOK crudtype", crudtype)
    permission_required = 'projects.add_project'
    # permission_required = set_required_rights('projects', 'projectform')

    return permission_required
