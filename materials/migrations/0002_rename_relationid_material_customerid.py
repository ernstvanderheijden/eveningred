# Generated by Django 4.1.5 on 2023-02-22 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='relationid',
            new_name='customerid',
        ),
    ]
