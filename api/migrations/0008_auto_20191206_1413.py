# Generated by Django 3.0 on 2019-12-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191206_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='uid',
            field=models.CharField(default='45f5247b08b39a647ced0c2ed77ab89e', editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='uid',
            field=models.CharField(default='3388e435034115d1996ff87098480cbe', editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastermachine',
            name='uid',
            field=models.CharField(default='f4393c59154c13ac9037267fef0f1b70', editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='masterplant',
            name='uid',
            field=models.CharField(default='2892391b9c388663d5cc4afc9f38da52', editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
        migrations.AlterField(
            model_name='mastersku',
            name='uid',
            field=models.CharField(default='8faaea8fb772ed3fc447ad56bb070685', editable=False, max_length=50, verbose_name='Master Plant Uid'),
        ),
    ]
