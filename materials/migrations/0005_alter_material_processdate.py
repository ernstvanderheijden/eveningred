# Generated by Django 4.1.5 on 2023-03-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_remove_material_amountmaterials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='processdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
