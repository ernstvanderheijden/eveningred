from articles.models import Article
from configuration.models import Configuration
from core.middleware import local
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from emails.models import Email
from hours.models import Hour
from master.models import \
    Articlegroup, \
    Conditiontype, \
    Paymenttype, \
    Unittype, \
    Vattype
from materials.models import Material
from projects.models import Project
from relations.models import Relation
from shared.functions import update_address, get_fulladdress
from users.models import User


def update_instance(instance):
    if instance.creatorid is None and hasattr(local, 'user'):
        if local.user.id:
            instance.creatorid_id = local.user.id
    if hasattr(local, 'user'):
        if local.user.id:
            instance.updaterid_id = local.user.id


# Article
@receiver(pre_save, sender=Article)
def save_cre_and_upd_article(sender, instance, **kwargs):
    update_instance(instance)


# Articlegroup
@receiver(pre_save, sender=Articlegroup)
def save_cre_and_upd_articlegroup(sender, instance, **kwargs):
    update_instance(instance)


# Conditiontype
@receiver(pre_save, sender=Conditiontype)
def save_cre_and_upd_conditiontype(sender, instance, **kwargs):
    update_instance(instance)


# Configuration
@receiver(pre_save, sender=Configuration)
def save_cre_and_upd_configuration(sender, instance, **kwargs):
    update_instance(instance)
    if Configuration.objects.all().count() == 0:
        instance.is_default = True


# Email
@receiver(pre_save, sender=Email)
def save_cre_and_upd_email(sender, instance, **kwargs):
    update_instance(instance)


# Hour
@receiver(pre_save, sender=Hour)
def save_cre_and_upd_hour(sender, instance, **kwargs):
    update_instance(instance)


# Material
@receiver(pre_save, sender=Material)
def save_cre_and_upd_material(sender, instance, **kwargs):
    update_instance(instance)


# Paymenttype
@receiver(pre_save, sender=Paymenttype)
def save_cre_and_upd_paymenttype(sender, instance, **kwargs):
    update_instance(instance)


# Project
@receiver(pre_save, sender=Project)
def save_cre_and_upd_projcet(sender, instance, **kwargs):
    update_instance(instance)
    update_address(instance)


# Relation
@receiver(pre_save, sender=Relation)
def save_cre_and_upd_relation(sender, instance, **kwargs):
    update_instance(instance)
    instance.fulladdress = get_fulladdress(instance.street, instance.number, instance.suffix, instance.postalcode, instance.city)


# Unittype
@receiver(pre_save, sender=Unittype)
def save_cre_and_upd_unittype(sender, instance, **kwargs):
    update_instance(instance)


# User
@receiver(pre_save, sender=User)
def save_cre_and_upd_user(sender, instance, **kwargs):
    if hasattr(local, 'user'):  # If user created from the commandline
        if str(local.user) != "AnonymousUser":
            update_instance(instance)


# Vattype
@receiver(pre_save, sender=Vattype)
def save_cre_and_upd_vattype(sender, instance, **kwargs):
    update_instance(instance)
