from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from core.check_deny_delete_or_update import check_deny_del_or_upd


# Maintenance related
class Articlegroup(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=True, null=True, max_length=50)
    # orderingid = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_articlegroup')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_articlegroup')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            "articles":
                {
                    "package": 'articles',
                    "model": 'Article',
                    "namefield": "articlegroupid",
                },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)


# Maintenance related
class Conditiontype(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=True, null=True, max_length=50)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_conditiontype')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_conditiontype')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            "configuration":
                {
                    "package": 'configuration',
                    "model": 'Configuration',
                    "namefield": "conditiontypeid",
                },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)


# Finance related
class Paymenttype(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=False, null=False, max_length=50)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_paymenttype')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_paymenttype')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            "configuration":
                {
                    "package": 'configuration',
                    "model": 'Configuration',
                    "namefield": "paymenttypeid",
                },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)


# Finance related
class Unittype(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=False, null=False, max_length=50)
    unit = models.CharField(blank=False, null=False, max_length=50)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_unittype')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_unittype')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            "articles":
                {
                    "package": 'articles',
                    "model": 'Article',
                    "namefield": "unittypeid",
                },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)


class Vattype(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=False, null=False, max_length=50)
    vatcode = models.PositiveIntegerField(null=False, blank=False)
    percentage_description = models.CharField(blank=True, null=True, max_length=50)
    percentage = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_vattype')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_vattype')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            "articles":
                {
                    "package": 'articles',
                    "model": 'Article',
                    "namefield": "vattypeid",
                },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
