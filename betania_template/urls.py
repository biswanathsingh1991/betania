from django.contrib import admin
from django.urls import path
from betania_template.views.index import IndexTemplateView
from betania_template.views.login import LoginTemplateView

app_name = 'betania_template'


urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index_temp"),
    path('login.html/', LoginTemplateView.as_view(), name="index_temp"),

]
