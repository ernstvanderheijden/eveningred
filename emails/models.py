from django.db import models

from core.check_deny_delete_or_update import check_deny_del_or_upd


class Email(models.Model):
    EMAILSTATUS_CHOICES = (
        (0, 'Ready to send'),
        (9, 'Send'),
    )
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='f_mail_user')
    to_email = models.CharField(max_length=255, blank=True, null=True)
    cc_email = models.CharField(max_length=255, blank=True, null=True)
    bcc_email = models.CharField(max_length=255, blank=True, null=True)
    from_email = models.CharField(max_length=255, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    mail_subject = models.CharField(max_length=100, default="", null=True, blank=True)
    plain_message = models.TextField(null=True, blank=True)
    html_message = models.TextField(null=True, blank=True)
    attachments = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=0, choices=EMAILSTATUS_CHOICES, null=False, blank=False)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    creatorid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='creatorid_email')
    updaterid = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.PROTECT, related_name='updaterid_email')

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)

    @staticmethod
    def dependencies(pk):
        models_link_dictionary = {
        }
        return check_deny_del_or_upd(pk, models_link_dictionary)
