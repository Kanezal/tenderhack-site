from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('chat/<int:room_id>/', views.chat_view, name='chat'),
    path('contacts/', views.contacts_view, name='contacts'),
]