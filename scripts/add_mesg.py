
from api.models import MasterPlant, MasterMachine, MasterSku, MachineDetail
import random
import secrets

import random
import string

from django.utils.text import slugify


def unique_uid_generator(size=12, chars=string.digits + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def run():
    for i in MasterMachine.objects.all():
        for x in range(100):
            print(x)
            sku = MasterSku.objects.order_by('?').first()
            uid1 = unique_uid_generator()
            l = ("accept", "reject")
            MachineDetail.objects.create(
                sku=sku,
                machine=i,
                box_weight=random.randint(200, 300),
                pass_status=random.choice(l),
                box_count=random.randint(100, 200),
                timestamp=f'timestamp{x}',
            )
