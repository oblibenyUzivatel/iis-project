# Generated by Django 2.0.5 on 2018-11-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kavarna', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reaction',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='reaction',
            name='score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]