# Generated by Django 3.0 on 2019-12-07 09:08

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20191207_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='uid',
            field=models.CharField(default=api.models.unique_uid_generator, editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='uid',
            field=models.CharField(default=api.models.unique_uid_generator, editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastermachine',
            name='uid',
            field=models.CharField(default=api.models.unique_uid_generator, editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='masterplant',
            name='uid',
            field=models.CharField(default=api.models.unique_uid_generator, editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastersku',
            name='uid',
            field=models.CharField(default=api.models.unique_uid_generator, editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
    ]
