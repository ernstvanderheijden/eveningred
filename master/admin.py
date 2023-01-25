from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Articlegroup, Conditiontype, Paymenttype, Unittype, Vattype


@admin.register(Articlegroup)
class ArticlegroupAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Articlegroup._meta.fields]
    search_fields = ["id", "description"]
    pass


@admin.register(Conditiontype)
class ConditiontypeAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Conditiontype._meta.fields]
    search_fields = ["id", "description"]
    pass


@admin.register(Paymenttype)
class PaymenttypeAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Paymenttype._meta.fields]
    search_fields = ["id", "description"]
    pass


@admin.register(Unittype)
class UnittypeAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Unittype._meta.fields]
    search_fields = ["id", "description"]
    pass


@admin.register(Vattype)
class VattypeAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Vattype._meta.fields]
    search_fields = ["id", "description"]
    pass
