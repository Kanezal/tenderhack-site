from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
