

from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import (MachineDetail, MasterSku,
                        MasterMachine, MasterPlant, Location)
from rest_framework import serializers


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterSku
        fields = "__all__"


class SkuIdListView(ListAPIView):

    serializer_class = SkuSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        return MasterSku.objects.all()
