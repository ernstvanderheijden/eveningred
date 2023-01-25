from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Email


@admin.register(Email)
class EmailAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Email._meta.fields]
    search_fields = ["id", "to_email", "cc_email", "bcc_email", "mail_subject"]
    pass
