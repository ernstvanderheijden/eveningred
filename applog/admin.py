from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Applog


@admin.register(Applog)
class ApplogAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Applog._meta.fields]
    search_fields = ["id", "app_name", "model_name", "message", "reason", "severity"]
    pass
