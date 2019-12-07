from rest_auth.registration.views import RegisterView
from register.models import UserProfile
from api.models import MasterPlant
from rest_framework.response import Response
from rest_framework import status


class SignUpView(RegisterView):

    def create_profile(self, user, plant_uid):

        UserProfile.objects.create(
            user=user,
            plant_staff=MasterPlant.objects.get(uid=plant_uid)
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        self.create_profile(user, request.data.get('plant_uid'))
        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)
