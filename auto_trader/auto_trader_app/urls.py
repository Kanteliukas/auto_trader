from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('car_ads/', views.CarAdsListView.as_view(), name='car_ads'),
]
