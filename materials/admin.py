from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Material


@admin.register(Material)
class EstateAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Material._meta.fields]
    search_fields = ["id", "description"]
    pass
