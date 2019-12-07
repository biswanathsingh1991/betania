# Generated by Django 3.0 on 2019-12-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191206_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='uid',
            field=models.UUIDField(default='73c2c2b2ffb945ee77ae1c6b64da1ab4', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='uid',
            field=models.UUIDField(default='81e6174e0a7a7fe3eb5e3776278acf68', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastermachine',
            name='uid',
            field=models.UUIDField(default='792f53636549e30cabb5899aca8ea10c', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='masterplant',
            name='uid',
            field=models.UUIDField(default='0c29cfe814c6c16f63338773966f3994', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastersku',
            name='uid',
            field=models.UUIDField(default='b68a1e6e5e82db253ff308d86197e358', editable=False, verbose_name='Master Plant Uid'),
        ),
    ]