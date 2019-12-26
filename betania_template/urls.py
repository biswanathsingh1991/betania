from django.contrib import admin
from django.urls import path
from betania_template.views.index import IndexTemplateView
from betania_template.views.login import LoginTemplateView

app_name = 'betania_template'


urlpatterns = [
    path('dkf/', IndexTemplateView.as_view(), name="index_temp"),
    path('index.html/', IndexTemplateView.as_view(), name="index3_temp"),
    path('login.html/', LoginTemplateView.as_view(), name="login_temp"),

]
