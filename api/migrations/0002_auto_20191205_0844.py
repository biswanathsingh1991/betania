# Generated by Django 3.0 on 2019-12-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastermachine',
            name='mm_id',
            field=models.CharField(default='', max_length=200, verbose_name='Machine Id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='uid',
            field=models.UUIDField(default='81f2a8f6ef664452716d2262cafec450', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='uid',
            field=models.UUIDField(default='f9e27846c0d00f3501fca48439bd443f', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastermachine',
            name='uid',
            field=models.UUIDField(default='e11b2e70d88b6bfdc1653c2410067ff6', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='masterplant',
            name='uid',
            field=models.UUIDField(default='3fa5b3c9c6f2490eb11df63282f3e85b', editable=False, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastersku',
            name='uid',
            field=models.UUIDField(default='0d3db874780525b7a9602b8382e78858', editable=False, verbose_name='Master Plant Uid'),
        ),
    ]
