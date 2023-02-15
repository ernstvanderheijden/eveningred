from core.globals.global_functions import decode_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def actions(request):
    data = dict()
    ctx = dict()
    ctx['action'] = request.GET.get('action', '')
    ctx['level'] = request.GET.get('level', 0)
    ctx['pk'] = request.GET.get('pk', '')
    if ctx['pk']:
        ctx['pk'] = int(ctx['pk'])
    ctx['successurl'] = request.GET.get('successurl', '')
    if ctx['successurl']:
        data['successurl'] = decode_string(ctx['successurl'])
    data['level'] = request.GET.get('level', 0)
    data['fragment'] = request.GET.get('fragment', '')
    match ctx['action']:

        case 'usersendinvitation':
            from shared.user import user_send_invitation
            if user_send_invitation(request):
                data['messagelist'] = ["Uitnodiging verstuurd", "success", "short"]  # messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'
                data['form_is_valid'] = True
            else:
                data['messagelist'] = ["Uitnodiging niet verstuurd", "danger"]
                data['form_is_valid'] = False

        case _:
            data['messagelist'] = ["Geen juiste actie opgegeven", "danger"]
            data['form_is_valid'] = False

    return JsonResponse(data)
