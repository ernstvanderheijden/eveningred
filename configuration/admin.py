from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Configuration


@admin.register(Configuration)
class ConfigurationAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Configuration._meta.fields]
    pass
