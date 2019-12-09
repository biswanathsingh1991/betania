

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
from datetime import datetime, timedelta, date


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineDetail
        exclude = ("timestamp_modified", )


class MessageFilter(filters.FilterSet):
    sku = filters.CharFilter(field_name="sku", method="skufilter")
    day = filters.NumberFilter(
        field_name="timestamp_created", method="dayfilter")

    class Meta:
        model = MachineDetail
        fields = ["pass_status", "box_count",
                  "box_weight", "timestamp_created"]

    def skufilter(self, queryset, filedname, value):
        return queryset.filter(sku__uid=value)

    def dayfilter(self, queryset, fieldname, value):
        return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(days=30 if n is None else int(value)),
            datetime.now()
        ))


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

    def parsedata(self, data, queryset):

        nq = MachineDetail.objects.filter(
            machine__plant__uid=self.request.user.userprofile.plant_staff.uid
        )
        sku_id = MasterSku.objects.get(uid=self.request.GET.get("sku"))
        data_dict = {}
        for i in data:
            data_dict[f't{i.get("id")}'] = i
        return {
            "total_msg": len(data),
            "total_machine_msg":  nq.count(),
            'total_accept': nq.filter(pass_status='accept').count(),
            'total_reject': nq.filter(pass_status='reject').count(),
            "filter_accept": queryset.filter(pass_status="accept").count(),
            "filter_reject": queryset.filter(pass_status="accept").count(),
            "day": int(self.request.GET.get('day', 30)),
            "sku": sku_id.name,
            "sku_ul": sku_id.ul,
            "sku_ll": sku_id.ll,
            "data": data_dict,
        }

    def get_queryset(self):
        plant = self.request.user.userprofile.plant_staff
        return MachineDetail.objects.filter(machine__plant__uid=plant.uid)
        # return MachineDetail.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.parsedata(serializer.data, queryset))
