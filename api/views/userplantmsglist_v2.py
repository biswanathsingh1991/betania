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
    

    class Meta:
        model = MachineDetail
        fields = ["pass_status", "box_count",
                  "box_weight", "timestamp_created"]

    def skufilter(self, queryset, filedname, value):
        return queryset.filter(sku__uid=value)

    def dayfilter(self, queryset, fieldname, value):
        return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(days=30 if value is None else int(value)),
            datetime.now()
        ))


class UserPlantMessageListViewV2(ListAPIView):

    serializer_class = MessageSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = (TokenAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,
                       OrderingFilter, SearchFilter)
    filterset_class = MessageFilter

    def getSkuData(self, plant):
        sku = {}
        for i in MasterSku.objects.all():
            k = MachineDetail.objects.filter(machine__plant__uid=plant.uid)
            sku[i.name] = {
                "total": k.count(),
                "accept": k.filter(pass_status="accept").count(),
                "rejtect": k.filter(pass_status="reject").count(),
            }
        return sku

    def parsedata(self, data, queryset, plant):

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
            "filter_reject": queryset.filter(pass_status="reject").count(),
            "sku": sku_id.name,
            "Location": plant.name,
            "plant_name": plant.loc.loc,
            "sku_ul": sku_id.ul,
            "sku_ll": sku_id.ll,
            "sku_data": self.getSkuData(plant),
            "data": data_dict,

        }

    def dayfilter(self, queryset, value):
    	return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(days=30 if value is None else int(value)),
            datetime.now()
        ))
    def time_filter(self, queryset, hours):
        return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(hours=int(hours)),
    		datetime.now()
        ))

    def time_stamp_filter(self, queryset, t1, t2):
    	tim1 = datetime.strptime(t1, "%d%m%Y")
    	tim2=datetime.strptime(t2, "%d%m%Y")
    	return queryset.filter(timestamp_created__range=(tim1,tim2))
    	return queryset

    def return_query_set(self, queryset, request):
    	filter_type=request.GET.get("type")
    	if (filter_type=="d"):
    		return self.dayfilter(queryset, request.GET.get("days"))
    	elif (filter_type=="h"):
    		return self.time_filter(queryset, request.GET.get("hours"))
    	elif (filter_type=="s"):
    		return self.time_stamp_filter(queryset, request.GET.get("t1"), request.GET.get("t2"))
    	else:
    		return queryset

    	return queryset


    def get_queryset(self):
        plant = self.request.user.userprofile.plant_staff
        mainquery =  MachineDetail.objects.filter(machine__plant__uid=plant.uid)
        return self.return_query_set(mainquery, self.request)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(self.parsedata(serializer.data, queryset, self.request.user.userprofile.plant_staff))
