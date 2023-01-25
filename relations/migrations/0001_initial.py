# Generated by Django 4.1.5 on 2023-01-20 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationname', models.CharField(max_length=50)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('placeofbirth', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('street', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('number', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('suffix', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('postalcode', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('fulladdress', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('iban', localflavor.generic.models.IBANField(blank=True, include_countries=None, max_length=34, null=True, use_nordea_extensions=False)),
                ('bic', localflavor.generic.models.BICField(blank=True, max_length=11, null=True)),
                ('is_master', models.BooleanField(default=False)),
                ('is_debtor', models.BooleanField(default=False)),
                ('is_creditor', models.BooleanField(default=False)),
                ('debtornr', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('creditornr', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('vatnr', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('cocnr', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('licenseplate', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('sendmethod', models.IntegerField(choices=[(1, 'E-mail'), (2, 'Print')])),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('conditiontypeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='conditiontypeid_relation', to='master.conditiontype')),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_relation', to=settings.AUTH_USER_MODEL)),
                ('paymenttypeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paymenttypeid_relation', to='master.paymenttype')),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_relation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['relationname'],
            },
        ),
    ]
