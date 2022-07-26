from .models import CarAd, Images
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


class NewCreateAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = (
            "car_model",
            "year",
            "fuel_type",
            "transmission_type",
            "price",
        )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
    )

    class Meta:
        model = Images
        fields = ("image",)
