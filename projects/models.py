from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models
from shared.functions import get_fulladdress


class Project(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=True, null=True, max_length=100)
    startdate = models.DateField(blank=True, null=True)
    relationid = models.ForeignKey('relations.Relation', null=True, blank=True, on_delete=models.PROTECT, related_name='relationid_project')
    street = models.CharField(max_length=50, default="", null=True, blank=True)
    number = models.CharField(max_length=6, default="", null=True, blank=True)
    suffix = models.CharField(max_length=6, default="", null=True, blank=True)
    postalcode = models.CharField(max_length=6, default="", null=True, blank=True)
    city = models.CharField(max_length=50, default="", null=True, blank=True)
    fulladdress = models.CharField(max_length=120, default="", null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_project')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_project')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.fulladdress = get_fulladdress(self.street, self.number, self.suffix, self.postalcode, self.city)
        super(Project, self).save(*args, **kwargs)

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
