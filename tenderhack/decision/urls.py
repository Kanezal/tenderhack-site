from django.urls import path
from .views import update_main_contract, view_history

urlpatterns = [
    path('update_contract/<int:pk>/', update_main_contract, name='update_contract'),
    path('history/<int:pk>/', view_history, name='history'),
]