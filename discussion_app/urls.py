from django.urls import path
from .views import room, roomhome, createRoom, updateRoom, deleteRoom, deleteMessage, userProfile, updateUser,topicsPage, activityPage
urlpatterns = [
    path('Roomhome', roomhome, name='roomhome'),
    path('room/<str:pk>/', room, name='room'),
    path('user-profile/<str:pk>/', userProfile, name='user-profile'),
    path('create-room', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', deleteMessage, name='delete-message'),
    path('update-user', updateUser, name='update-user'),
    path('topics/', topicsPage, name='topics'),
    path('activity/', activityPage, name='activity'),
]



