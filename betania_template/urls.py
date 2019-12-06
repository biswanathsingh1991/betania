from django.contrib import admin
from django.urls import path
from betania_template.views.index import IndexTemplateView
app_name = 'betania_template'


urlpatterns = [
    path('index/', IndexTemplateView.as_view(), name="index_temp"),
]
