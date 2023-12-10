from django.urls import path
from . import views

urlpatterns = [
    path('update_contract/<int:pk>/', views.update_main_contract, name='update_contract'),
    path('history/<int:pk>/', views.view_history, name='history'),

    path('approve_change/<int:pk>/', views.approve_change, name='approve_change'),
    path('reject_change/<int:pk>/', views.reject_change, name='reject_change'),
]