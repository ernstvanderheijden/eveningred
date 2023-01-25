from core.check_deny_delete_or_update import check_deny_del_or_upd
from django.db import models


class Article(models.Model):
    STATUS_CHOICES = (
        (0, 'Actief'),
        (-1, 'Inactief'),
    )
    description = models.CharField(blank=False, null=False, max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    unittypeid = models.ForeignKey('master.Unittype', null=False, blank=False, on_delete=models.PROTECT, related_name='unittypeid_article')
    articlegroupid = models.ForeignKey('master.Articlegroup', null=False, blank=False, on_delete=models.PROTECT, related_name='articlegroupid_article')
    vattypeid = models.ForeignKey('master.Vattype', null=False, blank=False, on_delete=models.PROTECT, related_name='vattypeid_article')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_article')
    updaterid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_article')

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return self.description

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
