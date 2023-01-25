from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass


class Version(models.Model):
    static_version = models.IntegerField(default=1, blank=False, help_text="version of the static files")

    class Meta:
        ordering = ["id"]
        verbose_name = "Versienummer"
        verbose_name_plural = 'Versienummers'
