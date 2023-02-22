from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Hour


@admin.register(Hour)
class EstateAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Hour._meta.fields]
    search_fields = ["id", "description"]
    pass
