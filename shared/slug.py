from secrets import token_urlsafe
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def set_slug(recordid):
    return urlsafe_base64_encode(force_bytes(recordid) + force_bytes(settings.SECRET_KEY) + force_bytes(token_urlsafe(16)))
