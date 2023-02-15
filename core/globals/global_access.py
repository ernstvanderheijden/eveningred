from core.globals.global_functions import is_ajax_request
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.views import redirect_to_login
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect


class UserAccessMixin(PermissionRequiredMixin):
    permission_required = ''
    # raise_exception = False
    # permission_denied_message = "Geen rechten hiervoor"
    # login_url = '/'
    # redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        self.permission_required = set_required_permissions(request)

        # print("PLOK self.has_permission()", self.has_permission())
        if not self.has_permission():
            if is_ajax_request(request):
                data = dict()
                return JsonResponse(data)
            else:
                return redirect('/403/')

        # permissions = Permission.objects.filter(Q(user=request.user) | Q(group__user=request.user)).all()
        # print("PLOK permissions", permissions)
        # for p in permissions:
        #     print("PLOK permissions", p, request.user)
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


def set_required_permissions(request):
    package = ''
    chapter = ''
    nameform = ''
    crudtype = ''

    if '/template/' in request.path:
        crudtype = 'view'
    elif '/create/' in request.path:
        crudtype = 'add'
    elif '/update/' in request.path:
        crudtype = 'change'
    if '/delete/' in request.path:
        crudtype = 'delete'

    request_items = dict()
    for key, value in request.GET.items():
        request_items.update({key: value})
    if 'package' in request_items:
        package = request_items['package']
    if 'chapter' in request_items:
        chapter = request_items['chapter']
    if 'nameform' in request_items:
        nameform = request_items['nameform']

    modelname = nameform.replace('form', '')
    if not modelname:
        modelname = get_modelname(package, chapter)

    if package == 'dashboard' and chapter == 'detail':
        permission_required = 'auth.view_permission'
    elif package == 'users' and chapter == 'myprofile':
        permission_required = 'auth.view_permission'
    elif package == 'users' and nameform == 'userprofileform':
        permission_required = 'auth.view_permission'
    # elif not crudtype:
    #     permission_required = 'auth.view_permission'
    else:
        print('PLOK nameform', nameform)
        match nameform:
            case 'some_form':
                print("PLOK some_form")
                permission_required = 'auth.view_permission'
            case _:
                permission_required = package + '.' + crudtype + '_' + modelname
    return permission_required


def get_modelname(package, chapter):
    if package == 'dashboard':
        modelname = 'dashboard'
    elif package == 'applog':
        modelname = 'dashboard'
    elif package == 'article':
        modelname = 'dashboard'
    elif package == 'configuration':
        modelname = 'dashboard'
    elif package == 'master':
        modelname = chapter[4:len(chapter)]
    else:
        modelname = package[0:(len(package)-1)]
    return modelname
