import django_filters
from .models import CarAd


class CarAdFilter(django_filters.FilterSet):
    class Meta:
        model = CarAd
        fields = (
            "car_model",
            "fuel_type",
            "transmission_type",
            "price",
            "year",
        )
