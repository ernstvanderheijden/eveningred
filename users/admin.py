from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)


# @admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in User._meta.fields]
    search_fields = ["id", "username", "first_name", "last_name"]
    pass
