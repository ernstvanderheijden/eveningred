# Generated by Django 4.1.5 on 2023-01-20 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vattype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('vatcode', models.PositiveIntegerField()),
                ('percentage_description', models.CharField(blank=True, max_length=50, null=True)),
                ('percentage', models.DecimalField(decimal_places=1, max_digits=3)),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_vattype', to=settings.AUTH_USER_MODEL)),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_vattype', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Unittype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_unittype', to=settings.AUTH_USER_MODEL)),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_unittype', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Paymenttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_paymenttype', to=settings.AUTH_USER_MODEL)),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_paymenttype', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Conditiontype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_conditiontype', to=settings.AUTH_USER_MODEL)),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_conditiontype', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Articlegroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Actief'), (-1, 'Inactief')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creatorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='creatorid_articlegroup', to=settings.AUTH_USER_MODEL)),
                ('updaterid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updaterid_articlegroup', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
    ]
