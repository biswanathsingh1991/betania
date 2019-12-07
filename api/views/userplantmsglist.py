

from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import (MachineDetail, MasterSku,
                        MasterMachine, MasterPlant, Location)
from rest_framework import serializers
from rest_framework.authentication import (
    BaseAuthentication, TokenAuthentication)
from register.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import (OrderingFilter, SearchFilter)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineDetail
        fields = "__all__"
        depth = 2


class MessageFilter(filters.FilterSet):
    sku = filters.CharFilter(field_name="sku", method="skufilter")

    class Meta:
        model = MachineDetail
        fields = ["pass_status", "box_count", "box_weight"]

    def skufilter(self, queryset, filedname, value):
        print("from queryset")
        print(queryset)
        print(value)
        return queryset.filter(sku__uid=value)


class UserPlantMessageListView(ListAPIView):

    serializer_class = MessageSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = (TokenAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)
    permission_classes = ()
    filter_backends = (filters.DjangoFilterBackend,
                       OrderingFilter, SearchFilter)
    filterset_class = MessageFilter

    def get_queryset(self):
        plant = self.request.user.userprofile.plant_staff
        return MachineDetail.objects.filter(machine__plant__uid=plant.uid)
        # return MachineDetail.objects.all()
