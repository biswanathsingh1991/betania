from django.contrib import admin
from .models import (Location, MasterPlant, MasterSku,
                     MasterMachine, MachineDetail)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('__str__', "state", "country", "uid",)

    class Meta:
        model = Location


class MasterPlantAdmin(admin.ModelAdmin):
    list_display = ('__str__', "loc", "uid",)

    class Meta:
        model = MasterPlant


class MasterSkuPlantAdmin(admin.ModelAdmin):
    list_display = ('__str__', "ul", "ll", "uid")

    class Meta:
        model = MasterSku


class MasterMachineAdmin(admin.ModelAdmin):
    list_display = ('__str__', "plant", "uid")

    class Meta:
        model = MasterMachine


class MachineDetailAdmin(admin.ModelAdmin):
    list_display = ('__str__', "pass_status", "box_count",
                    "box_weight", "timestamp", "uid", "timestamp_created",)

    class Meta:
        model = MachineDetail


admin.site.register(MasterPlant, MasterPlantAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(MasterSku, MasterSkuPlantAdmin)
admin.site.register(MasterMachine, MasterMachineAdmin)
admin.site.register(MachineDetail, MachineDetailAdmin)
