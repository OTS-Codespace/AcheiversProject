from django.contrib import admin
from django.urls import path
from user_manager_app import registration
from django.conf import settings
from django.conf.urls.static import static

# Please, put all the urls specific to user_manager_app here
urlpatterns = [
    path('register/', registration.register, name='register'),
]
