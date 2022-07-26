from .models import CarAd
from django import forms


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = (
            "car_model",
            "year",
            "fuel_type",
            "transmission_type",
            "price",
        )
