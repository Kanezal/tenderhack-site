from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.market_view, name='market'),
    path('detail/<int:id>/', views.detail_view, name='proposal_detail'),
]
