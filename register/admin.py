from django.contrib import admin

from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'plant_staff', )

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
