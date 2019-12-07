
from api.models import MasterPlant, MasterMachine
import random
import secrets

import random
import string

from django.utils.text import slugify


def unique_uid_generator(size=12, chars=string.digits + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def run():
    for i in MasterPlant.objects.all():
        for x in range(4):
            uid1 = unique_uid_generator()
            MasterMachine.objects.create(
                name=uid1,
                mm_id=uid1,
                plant=i,

            )
