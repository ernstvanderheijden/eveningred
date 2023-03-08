from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models


class Material(models.Model):
    description = models.CharField(null=True, blank=True, max_length=255)
    projectid = models.ForeignKey("projects.Project", null=False, blank=False, on_delete=models.PROTECT, related_name='projectid_material')
    userid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='userid_material')
    customerid = models.ForeignKey("relations.Relation", null=True, blank=True, on_delete=models.PROTECT, related_name='relationid_material')
    issuedate = models.DateField(null=True)
    purchasingcosts = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    processdate = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_material')
    updaterid = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_material')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

    @staticmethod
    def dependencies(pk):
        if pk:
            material = Material.objects.get(id=pk)
            if material.processdate:
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
