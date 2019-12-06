from django.contrib import admin
from django.urls import path
from api.views.create_message import CreateMessageView
from api.views.list_api import CreateMessageView
app_name = 'api'


urlpatterns = [
    path('test/', CreateMessageView.as_view(), name="create_message"),
    path('list/', CreateMessageView.as_view(), name="list_api"),
]
