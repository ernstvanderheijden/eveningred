from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Article._meta.fields]
    search_fields = ["id", "description"]
    pass
