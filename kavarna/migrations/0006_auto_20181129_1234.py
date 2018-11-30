# Generated by Django 2.1.2 on 2018-11-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kavarna', '0005_drinker_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='capacity',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='city',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='closesAt',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='housenumber',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='opensAt',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='psc',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='street',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]