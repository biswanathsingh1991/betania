
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import (MachineDetail, MasterSku, MasterMachine)


class CreateMessageView(GenericAPIView):

    allowed_methods = ("GET",)
    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):

        print('request recivec')
        print(request.GET.get('a'))
        print(request.GET.get('b'))
        print(request.GET.get('c'))
        print(request.GET.get('m').split(","))
        mess = request.GET.get('m').split("$")
        MachineDetail.objects.create(
            sku=MasterSku.objects.get(sku_id=request.GET.get('c')),
            machine=MasterMachine.objects.get(mm_id=request.GET.get('b')),
            box_count=mess[0],
            timestamp=mess[1],
            box_weight=mess[2],
            pass_status=mess[3],
        )
        return Response(status=status.HTTP_201_CREATED,)
