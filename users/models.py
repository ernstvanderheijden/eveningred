from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.functions import get_fullname


class User(AbstractUser):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    relationid = models.ForeignKey('relations.Relation', null=True, blank=True, on_delete=models.PROTECT, related_name='relationid_user')
    fullname = models.CharField(blank=True, null=True, max_length=100)
    insertion = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(null=False, blank=False, max_length=100, unique=True)
    is_manager = models.BooleanField(default=False, blank=False)
    is_employee = models.BooleanField(default=False, blank=False)
    is_employee_read = models.BooleanField(default=False, blank=False)
    is_employee_write = models.BooleanField(default=False, blank=False)
    is_owner = models.BooleanField(default=False, blank=False)
    paginatesize = models.IntegerField(default=25, null=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    creatorid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='creator_user')
    updaterid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='updater_user')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["fullname"]
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.fullname:
            return self.fullname
        else:
            return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.fullname = get_fullname(self.first_name, self.insertion, self.last_name)
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
