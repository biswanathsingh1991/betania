# Generated by Django 3.0 on 2019-12-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191206_1352'),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='plant_staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.MasterPlant', verbose_name='Plant'),
        ),
    ]