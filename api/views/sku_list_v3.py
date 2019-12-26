
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


class SkuIdListViewV3(GenericAPIView):

    serializer_class = SkuSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = (TokenAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated,)


    def dayfilter(self, queryset, value):
        return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(days=30 if value is None else int(value)),
            datetime.now()
        )).order_by('-timestamp_created')
    def time_filter(self, queryset, hours):
        return queryset.filter(timestamp_created__range=(
            datetime.now() - timedelta(hours=int(hours)),
            datetime.now()
        )).order_by('-timestamp_created')

    def time_stamp_filter(self, queryset, t1, t2):
        tim1 = datetime.strptime(t1, "%d%m%Y")
        tim2=datetime.strptime(t2, "%d%m%Y")
        return queryset.filter(timestamp_created__range=(tim1,tim2)).order_by('-timestamp_created')
        # return queryset.order_by('-timestamp_created')

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

    def get_time_filter_count(self, request, queryset, ul, ll):
        day = request.GET.get("day", 30)
        q1 = self.return_query_set(queryset, request)
        total_count = q1.count()
        total_accept = q1.filter(pass_status="accept").count()
        total_reject = q1.filter(pass_status="reject").count()
        over_weight = q1.filter(box_weight__gt=ul).count()
        under_weight = q1.filter(box_weight__lt=ll).count()
        in_range = q1.filter(box_weight__gt=ll, box_weight__lt=ul).count()
        return(day, total_count, total_accept, total_reject, over_weight, under_weight, in_range)

 

    def get(self, request, *args, **kwargs):
        plant = request.user.userprofile.plant_staff
        data = []
        for i in MasterSku.objects.all():
            sku_msg = MachineDetail.objects.filter(
                machine__plant__uid=plant.uid).filter(sku=i)
            filter_day, filter_total_count, filter_total_accept, filter_total_reject, filter_over_weight, filter_under_weight, in_range = self.get_time_filter_count(
                request, sku_msg, i.ul, i.ll)

            data_dict = {
                "sku_id": i.sku_id,
                "ul": i.ul,
                "ll": i.ll,
                "name": i.name,
                "uid": i.uid,
                "total_msg": sku_msg.count(),
                "total_msg_accept": sku_msg.filter(pass_status="accept").count(),
                "total_msg_reject": sku_msg.filter(pass_status="reject").count(),
                "total_over_weight": sku_msg.filter(box_weight__gt=i.ul).count(),
                "total_under_weight": sku_msg.filter(box_weight__lt=i.ll).count(),
                "total_weight_inrange": sku_msg.filter(box_weight__gt=i.ll, box_weight__lt=i.ul).count(),
                "filter_total_count": filter_total_count,
                "filter_total_accept": filter_total_accept,
                "filter_total_reject": filter_total_reject,
                "filter_over_weight": filter_over_weight,
                "filter_under_weight": filter_under_weight,
                "in_range": in_range

            }
            data.append(data_dict)
        return Response(data)
