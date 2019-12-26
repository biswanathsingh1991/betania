from rest_framework.permissions import BasePermission
from catalog.models import Product
from anonymousbuyer.models import Anonymousbuyer


class IsStaffUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.profile.staff_user:
            return True
        else:
            False