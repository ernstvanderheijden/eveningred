# Generated by Django 4.1.5 on 2023-02-24 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_material_creatorid_remove_material_projectid_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['description'], 'permissions': [('process_administration', 'Can process hours and materials to download')]},
        ),
    ]
