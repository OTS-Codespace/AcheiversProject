from django.contrib import admin
from django.urls import path
from user_manager_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Please, put all the urls specific to user_manager_app here






urlpatterns = [
   path('profile/', views.profile_view, name='profile'),
   path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
