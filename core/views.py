from core.functions.render_fragments import fragmentdatabuilder, confirmdatabuilder
from core.globals.global_access import UserAccessMixin
from core.globals.global_functions import decode_string
from core.globals.global_private_views import GlobalPrivateTemplate, GlobalPrivateCreate, GlobalPrivateUpdate, GlobalPrivateDelete
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect


class Template(UserAccessMixin, GlobalPrivateTemplate):
    pass


@login_required
def fragment(request):
    data = fragmentdatabuilder(request, {})
    return JsonResponse(data)


@login_required
def confirm(request):
    data = confirmdatabuilder(request, {})
    return JsonResponse(data)


class Create(UserAccessMixin, GlobalPrivateCreate):
    pass


class Update(UserAccessMixin, GlobalPrivateUpdate):
    pass


class Delete(UserAccessMixin, GlobalPrivateDelete):
    pass


@csrf_protect
@user_passes_test(lambda u: u.is_superuser)
def showctx(request):
    data = dict()
    ctx = dict()
    ctx['level'] = int(request.GET.get('level', 0))
    ctxdata = request.GET.get('ctxdata', '')
    ctx['contenttitle'] = "CTX"
    decoded_ctxdata = decode_string(ctxdata)
    ctx['ctxdata'] = decoded_ctxdata
    if 'successurl' in decoded_ctxdata:
        decoded_ctxdata['successurl_decoded'] = decode_string(decoded_ctxdata['successurl'])
    context = {'ctx': ctx}
    data['level'] = ctx['level'] + 1
    data['modalsize'] = "modalxl"
    data['fragment'] = 'body'
    data['html_header'] = render_to_string("core/modals/modalheader.html", context, request=request)
    data['html_body'] = render_to_string("core/ctx/ctx.html", context, request=request)
    data['html_footer'] = render_to_string("core/modals/modalfooter.html", context, request=request)
    data['form_is_valid'] = True
    return JsonResponse(data)
