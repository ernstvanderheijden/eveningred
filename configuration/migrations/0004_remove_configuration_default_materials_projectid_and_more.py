# Generated by Django 4.1.5 on 2023-02-22 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0003_alter_relation_sendmethod'),
        ('configuration', '0003_alter_configuration_default_materials_projectid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='default_materials_projectid',
        ),
        migrations.AddField(
            model_name='configuration',
            name='default_materials_customerid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='default_materials_customerid_configuration', to='relations.relation'),
        ),
    ]
