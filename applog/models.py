from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models


class Applog(models.Model):
    SEVERITY_CHOICES = (
        (5, 'Highest'),
        (4, 'High'),
        (3, 'Medium'),
        (2, 'Low'),
        (1, 'Lowest'),
    )
    version = models.PositiveIntegerField(default=1, null=False, blank=False)
    app_name = models.CharField(blank=True, null=True, max_length=50)
    model_name = models.CharField(blank=True, null=True, max_length=50)
    model_id = models.IntegerField(null=True, blank=True)
    reason = models.CharField(blank=True, null=True, max_length=50)
    messagetype = models.CharField(blank=True, null=True, max_length=20)
    message = models.JSONField(default=dict, null=True, blank=True)
    severity = models.IntegerField(default=3, choices=SEVERITY_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            # "invoiceline":
            #     {
            #         "package": 'invoices',
            #         "model": 'Invoiceline',
            #         "namefield": "articleid",
            #     },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
