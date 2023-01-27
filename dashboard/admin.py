from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Dashboard


@admin.register(Dashboard)
class EmailAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Dashboard._meta.fields]
    search_fields = ["id", "dashboard"]
