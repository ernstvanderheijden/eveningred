from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models


class Hour(models.Model):
    description = models.CharField(null=True, blank=True, max_length=255)
    projectid = models.ForeignKey("projects.Project", null=False, blank=False, on_delete=models.PROTECT, related_name='projectid_hour')
    userid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='userid_hour')
    issuedate = models.DateField(null=True)
    amounthours = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    processdate = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_hour')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_hour')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

    @staticmethod
    def dependencies(pk):
        if pk:
            hour = Hour.objects.get(id=pk)
            if hour.processdate:
                return True
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
