from django.contrib import admin
from django.urls import path
from register.views.signup import SignUpView

app_name = 'register'


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
]
