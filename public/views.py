from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from shared.email import create_email_user_invitation
from users.models import User


@csrf_exempt
def password_forgotten(request):
    ctx = dict()
    ctx['template_name'] = 'login/base_login.html'
    ctx['template_inner'] = 'login/password_forgotten.html'
    return render(request, ctx['template_name'], {'ctx': ctx})


@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        ctx = dict()
        ctx['template_name'] = 'login/base_login.html'
        ctx['template_inner'] = 'login/new_password_requested.html'
        post = request.POST.copy()
        ctx['emailaddress'] = post['emailaddress']
        try:
            user = User.objects.get(email=ctx['emailaddress'], is_active=True)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return render(request, ctx['template_name'], {'ctx': ctx})
        ctx['action_title'] = "Wijzig wachtwoord"
        create_email_user_invitation(user, [ctx['emailaddress']], user.first_name, ctx, attachments=None)
        return render(request, ctx['template_name'], {'ctx': ctx})
