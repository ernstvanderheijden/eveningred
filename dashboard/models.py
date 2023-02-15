from django.db import models


class Dashboard(models.Model):
    dashboard = models.CharField(max_length=100, default="Just needed for permissions", null=True, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_dashboard')
    updaterid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_dashboard')

    class Meta:
        ordering = ["dashboard"]

    def __str__(self):
        return self.dashboard
