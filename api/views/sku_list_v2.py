
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import (MachineDetail, MasterSku,
                        MasterMachine, MasterPlant, Location)
from rest_framework import serializers
from rest_framework.authentication import (
    BaseAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime, timedelta, date


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterSku
        fields = ("sku_id", "ul", "ll", "name", "uid")


class SkuIdListViewV2(GenericAPIView):

    serializer_class = SkuSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = (TokenAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_time_filter_count(self, request, queryset):
        day = request.GET.get("day", 30)
        q1 = queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(days=30 if day is None else int(day)),
            datetime.now()
        ))
        total_count = q1.count()
        total_accept = q1.filter(pass_status="accept").count()
        total_reject = q1.filter(pass_status="reject").count()
        return(day, total_count, total_accept, total_reject)

    def get(self, request, *args, **kwargs):
        plant = request.user.userprofile.plant_staff
        data = []
        for i in MasterSku.objects.all():
            sku_msg = MachineDetail.objects.filter(
                machine__plant__uid=plant.uid).filter(sku=i)
            filter_day, filter_total_count, filter_total_accept, filter_total_reject = self.get_time_filter_count(
                request, sku_msg)
            data_dict = {
                "sku_id": i.sku_id,
                "ul": i.ul,
                "ll": i.ll,
                "name": i.name,
                "uid": i.uid,
                "total_msg": sku_msg.count(),
                "total_msg_accept": sku_msg.filter(pass_status="accept").count(),
                "total_msg_reject": sku_msg.filter(pass_status="reject").count(),
                "filter_day": filter_day,
                "filter_total_count": filter_total_count,
                "filter_total_accept": filter_total_accept,
                "filter_total_reject": filter_total_reject,

            }
            data.append(data_dict)
        return Response(data)
