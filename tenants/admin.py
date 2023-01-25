from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Version


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    list_display = [f.name for f in Version._meta.fields]
    search_fields = ["id"]
    pass
