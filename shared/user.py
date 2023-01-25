from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.applog import save_applog
from shared.email import create_email_user_invitation
from users.models import User


def user_send_invitation(request):
    ctx = dict()
    pk = request.GET.get('pk', 0)
    action_performed = False
    record = get_object_or_404(User, pk=int(pk))
    if record:
        email = create_email_user_invitation(record, [record.email], record.first_name, ctx)
        save_applog('users', 'user', record.id, 'sent_email', 'user_invitation', 2, {"id": email.id})
        action_performed = True
        messages.success(request, "Verzonden")
    return action_performed
