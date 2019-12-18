from django.contrib import admin
from django.urls import path
from api.views.create_message import CreateMessageView
from api.views.locationplantlist import LocationPlantListView
from api.views.plantmachinelist import PlantMachineListView
from api.views.machinemsglist import MachineMsgListView
from api.views.plantmsglist import PlantMessageListView
from api.views.userplantmsglist import UserPlantMessageListView
from api.views.skulist import SkuIdListView
from api.views.sku_list_v2 import SkuIdListViewV2
from api.views.userplantmsglist_v2 import UserPlantMessageListViewV2
app_name = 'api'


urlpatterns = [
    path('Test/GetStringGetMethod',
         CreateMessageView.as_view(),
         name="create_message",
         ),

    path('loc/plant/list/<slug:uid>/',
         LocationPlantListView.as_view(),
         name="loc_plant_list",
         ),

    path('plant/machine/list/<slug:uid>/',
         PlantMachineListView.as_view(),
         name="plant_mach_list",
         ),

    path('machine/message/list/<slug:uid>/',
         MachineMsgListView.as_view(),
         name="mach_msg_list",
         ),

    path('plant/message/list/<slug:uid>/',
         PlantMessageListView.as_view(),
         name="plant_msg_list",
         ),

    path('user/plant/message/list/',
         UserPlantMessageListView.as_view(),
         name="user_plant_msg_list",
         ),
    path('skuid/list/', SkuIdListView.as_view(),
         name="skuid_list"),

    path('skuid/list/v2/', SkuIdListViewV2.as_view(),
         name="skuid_list"),

    path('user/plant/message/list/v2/', UserPlantMessageListViewV2.as_view(),
         name="user_plant_msg_listv2")
]
