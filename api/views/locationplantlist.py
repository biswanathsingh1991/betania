

from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import (MachineDetail, MasterSku,
                        MasterMachine, MasterPlant, Location)
from rest_framework import serializers


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterPlant
        fields = "__all__"
        depth = 2


class LocationPlantListView(ListAPIView):

    serializer_class = PlantSerializer
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        return Location.objects.get(uid=self.kwargs.get("uid")).masterplant_set.all()
