from django.db import models
from secrets import token_hex
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField)


class Location(models.Model):
    city = models.CharField(verbose_name="Location City", max_length=500)
    state = models.CharField(verbose_name="Location State", max_length=500)
    country = models.CharField(
        verbose_name="Location Country", default="India", max_length=500)
    loc = models.TextField(verbose_name="Meta data")
    uid = models.UUIDField(
        verbose_name="Master Plant Uid", default=token_hex(16), editable=False)
    timestamp_created = CreationDateTimeField()
    timestamp_modified = ModificationDateTimeField()

    def __str__(self):
        return self.city


class MasterPlant(models.Model):
    name = models.TextField(verbose_name="Master Plant Name")
    uid = models.UUIDField(
        verbose_name="Master Plant Uid", default=token_hex(16), editable=False)
    loc = models.ForeignKey(
        Location, verbose_name="Plant Location", on_delete=models.CASCADE)
    timestamp_created = CreationDateTimeField()
    timestamp_modified = ModificationDateTimeField()

    def __str__(self):
        return self.name


class MasterSku(models.Model):
    sku_id = models.CharField(verbose_name="Sku Name", max_length=200)
    ul = models.PositiveIntegerField(verbose_name="Sku Ul")
    ll = models.PositiveIntegerField(verbose_name="Sku ll")
    uid = models.UUIDField(
        verbose_name="Master Plant Uid", default=token_hex(16), editable=False)
    timestamp_created = CreationDateTimeField()
    timestamp_modified = ModificationDateTimeField()

    def __str__(self):
        return self.sku_id


class MasterMachine(models.Model):
    name = models.CharField(verbose_name="Machine NAME", max_length=10000)
    plant = models.ForeignKey(
        MasterPlant, verbose_name="plant", on_delete=models.CASCADE)
    mm_id = models.CharField(verbose_name="Machine Id", max_length=200)
    uid = models.UUIDField(
        verbose_name="Master Plant Uid", default=token_hex(16), editable=False)
    timestamp_created = CreationDateTimeField()
    timestamp_modified = ModificationDateTimeField()

    def __str__(self):
        return self.name


class MachineDetail(models.Model):
    pass_status_choices = (
        ("accept", "accept"),
        ("reject", "reject"),
    )
    sku = models.ForeignKey(
        MasterSku, verbose_name="Sku Id", on_delete=models.CASCADE)
    machine = models.ForeignKey(
        MasterMachine, verbose_name="Master Machine", on_delete=models.CASCADE)
    box_weight = models.CharField(max_length=200, verbose_name="Box Weight")
    timestamp = models.CharField(max_length=200, verbose_name="Timestamp")
    pass_status = models.CharField(
        max_length=100, verbose_name="Pass Status", choices=pass_status_choices)
    box_count = models.PositiveIntegerField()
    uid = models.UUIDField(
        verbose_name="Master Plant Uid", default=token_hex(16), editable=False)
    timestamp_created = CreationDateTimeField()
    timestamp_modified = ModificationDateTimeField()

    def __str__(self):
        return self.machine.mm_id
