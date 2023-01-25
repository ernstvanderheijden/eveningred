from django.core.exceptions import ValidationError
from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models


class DefaultManager(models.Manager):
    def get_queryset(self):
        return super(DefaultManager, self).get_queryset().filter(is_default=True)


class Configuration(models.Model):
    objects = models.Manager()
    default = DefaultManager()
    is_default = models.BooleanField(default=False, blank=False)
    days_in_front = models.PositiveIntegerField(default=0, null=False, blank=False)
    on_each_side = models.PositiveIntegerField(default=3, null=False, blank=False)
    on_ends = models.PositiveIntegerField(default=0, null=False, blank=False)

    conditiontypeid = models.ForeignKey('master.Conditiontype', null=False, blank=False, on_delete=models.PROTECT, related_name='conditiontypeid_configuration')
    paymenttypeid = models.ForeignKey('master.Paymenttype', null=False, blank=False, on_delete=models.PROTECT, related_name='paymenttypeid_configuration')

    email_display_name = models.CharField(max_length=50, default="Eveningred", null=False, blank=False)
    email_from = models.EmailField(max_length=100, default="noreply@bosschapp.nl", null=False, blank=False)
    email_reply_to = models.EmailField(max_length=100, default="info@bosschapp.nl", null=False, blank=False)
    email_logo = models.CharField(max_length=250, null=True, blank=True)
    email_to_accountancy = models.EmailField(max_length=100, null=True, blank=True)

    conditions = models.CharField(max_length=250, default="", null=True, blank=True)
    regulations = models.CharField(max_length=250, default="", null=True, blank=True)

    homepage = models.CharField(max_length=250, default="", null=True, blank=True)
    aboutuspage = models.CharField(max_length=250, default="", null=True, blank=True)
    contactpage = models.CharField(max_length=250, default="", null=True, blank=True)
    instagrampage = models.CharField(max_length=250, default="", null=True, blank=True)
    facebookpage = models.CharField(max_length=250, default="", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_configuration')
    updaterid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_configuration')

    class Meta:
        ordering = ["id"]

    def clean(self):
        super().clean()
        match self.is_default:
            case True:
                intid = 0
                if self.id:
                    intid = self.id
                if Configuration.objects.filter(is_default=True).exclude(id=intid).count() != 0:
                    raise ValidationError({
                        'is_default': ValidationError('Er kan maar 1 standaard configuratie zijn.')
                    })

    def __str__(self):
        return str(self.id)

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
