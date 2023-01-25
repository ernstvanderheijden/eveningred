from django.contrib.auth.mixins import LoginRequiredMixin
from core.globals.global_views import GlobalTemplate, GlobalCreate, GlobalUpdate, GlobalDelete


class GlobalPrivateTemplate(LoginRequiredMixin, GlobalTemplate):
    appid = 0


class GlobalPrivateCreate(LoginRequiredMixin, GlobalCreate):
    appid = 0


class GlobalPrivateUpdate(LoginRequiredMixin, GlobalUpdate):
    appid = 0


class GlobalPrivateDelete(LoginRequiredMixin, GlobalDelete):
    appid = 0
