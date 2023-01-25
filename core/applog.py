from applog.models import Applog


def save_applog(app_name, model_name, model_id, reason, messagetype, severity, message):
    applog = Applog()
    applog.app_name = app_name
    applog.model_name = model_name
    applog.model_id = model_id
    applog.reason = reason
    applog.messagetype = messagetype
    applog.severity = severity
    applog.message = message
    applog.save()
