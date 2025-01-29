from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Please, put all the urls specific to user_manager_app here



urlpatterns = [ 
    path('register', views.Register, name='register'),
    # url patterns for user roles
    path('instructor/dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

