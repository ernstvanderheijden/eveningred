from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Relation


@admin.register(Relation)
class RelationAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Relation._meta.fields]
    search_fields = ["id", "relationname", "fulladdress"]
    pass
