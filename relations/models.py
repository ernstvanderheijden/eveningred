from django.core.exceptions import ValidationError

from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models
from localflavor.generic.models import IBANField, BICField


class Relation(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    SENDMETHOD_CHOICES = (
        (1, 'E-mail'),
        (2, 'Print'),
    )
    relationname = models.CharField(blank=True, null=True, max_length=50)
    firstname = models.CharField(blank=True, null=True, max_length=50)
    lastname = models.CharField(blank=True, null=True, max_length=50)
    dateofbirth = models.DateField(blank=True, null=True)
    placeofbirth = models.CharField(max_length=100, default="", null=True, blank=True)
    street = models.CharField(max_length=50, default="", null=True, blank=True)
    number = models.CharField(max_length=6, default="", null=True, blank=True)
    suffix = models.CharField(max_length=6, default="", null=True, blank=True)
    postalcode = models.CharField(max_length=6, default="", null=True, blank=True)
    city = models.CharField(max_length=50, default="", null=True, blank=True)
    fulladdress = models.CharField(max_length=120, default="", null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    iban = IBANField(null=True, blank=True)
    bic = BICField(null=True, blank=True)
    is_master = models.BooleanField(default=False, blank=False)
    is_debtor = models.BooleanField(default=False, blank=False)
    is_creditor = models.BooleanField(default=False, blank=False)
    debtornr = models.CharField(max_length=15, default="", null=True, blank=True)
    creditornr = models.CharField(max_length=15, default="", null=True, blank=True)
    vatnr = models.CharField(max_length=15, default="", null=True, blank=True)
    cocnr = models.CharField(max_length=15, default="", null=True, blank=True)
    licenseplate = models.CharField(max_length=15, default="", null=True, blank=True)
    conditiontypeid = models.ForeignKey('master.Conditiontype', null=True, blank=True, on_delete=models.PROTECT, related_name='conditiontypeid_relation')
    paymenttypeid = models.ForeignKey('master.Paymenttype', null=True, blank=True, on_delete=models.PROTECT, related_name='paymenttypeid_relation')
    sendmethod = models.IntegerField(choices=SENDMETHOD_CHOICES, default=1, null=False, blank=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_relation')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_relation')

    class Meta:
        ordering = ["relationname"]

    def __str__(self):
        if self.relationname:
            return self.relationname
        else:
            return self.lastname

    def clean(self):
        super().clean()
        if self.relationname is None and self.lastname is None:
            raise ValidationError({
                'relationname': ValidationError("Of `Relatienaam` of `Achternaam `invullen.")
            })
        # match self.sendmethod:
        #     case 1:
        #         if self.email is None:
        #             raise ValidationError({
        #                 'sendmethod': ValidationError("Bij verzendmethode 'e-mail' is een e-mailadres verplicht.")
        #             })

    def save(self, *args, **kwargs):
        if self.licenseplate:
            self.licenseplate = self.licenseplate.upper()
        super(Relation, self).save(*args, **kwargs)

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
            # "model":
            #     {
            #         "package": 'packagename',
            #         "model": 'Model',
            #         "namefield": "fieldname",
            #         # "extra_filter": {},
            #     },
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
