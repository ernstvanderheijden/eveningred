# Generated by Django 4.1.5 on 2023-02-22 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_material_creatorid_remove_material_projectid_and_more'),
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='default_materials_projectid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='default_materials_projectid_configuration', to='projects.project'),
            preserve_default=False,
        ),
    ]
