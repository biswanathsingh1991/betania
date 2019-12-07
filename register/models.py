from django.db import models
from api.models import MasterPlant
# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, verbose_name="User Profile", on_delete=models.CASCADE)

    plant_staff = models.ForeignKey(
        MasterPlant, verbose_name="Plant", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
