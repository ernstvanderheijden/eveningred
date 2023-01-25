from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Project


@admin.register(Project)
class EstateAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Project._meta.fields]
    search_fields = ["id", "description"]
    pass
