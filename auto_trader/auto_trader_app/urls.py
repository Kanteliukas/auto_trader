from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("carads/", views.CarAdsListView.as_view(), name="car-ads"),
    path("carads/<int:pk>", views.CarAdDetailView.as_view(), name="car-ad-detail"),
    path("carads/new", views.new_car_ad, name="new-car-ad"),
]
