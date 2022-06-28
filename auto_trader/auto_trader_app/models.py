from django.db import models
from django.utils.translation import gettext_lazy as _


class CarType(models.Model):
    car_types = models.CharField(
        _("Car type"),
        max_length=200,
        help_text=_("Enter car type"),
    )

    verbose_name = _("Car type")
    verbose_name_plural = _("Car types")

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.car_types}"


class Maker(models.Model):
    maker = models.CharField(
        _("Car maker"),
        max_length=200,
        help_text=_("Enter car maker name"),
    )

    verbose_name = _("Car maker")
    verbose_name_plural = _("Car makers")

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.maker}"


class MakerModel(models.Model):
    maker = models.ForeignKey(
        Maker, on_delete=models.RESTRICT, related_name="maker_models"
    )
    car_type = models.ForeignKey(
        CarType, on_delete=models.RESTRICT, related_name="car_type"
    )
    model = models.CharField(
        _("Model"),
        max_length=200,
        help_text=_("Enter car model"),
    )

    verbose_name = _("Model")
    verbose_name_plural = _("Models")

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.model}"


class FuelType(models.Model):
    fuel_types = models.CharField(
        _("Fuel type"),
        max_length=200,
        help_text=_("Enter fuel type"),
    )

    verbose_name = _("Fuel type")
    verbose_name_plural = _("Fuel types")

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.fuel_types}"


class TransmissionType(models.Model):
    transmission_types = models.CharField(
        _("Transmission type"),
        max_length=200,
        help_text=_("Enter transmission type"),
    )

    verbose_name = _("Transmission type")
    verbose_name_plural = _("Transmission types")

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.transmission_types}"


class CarAd(models.Model):
    car_model = models.ForeignKey(
        MakerModel, on_delete=models.SET_NULL, null=True, related_name="car_model"
    )
    fuel_type = models.ForeignKey(
        FuelType, on_delete=models.SET_NULL, null=True, related_name="fuel_type"
    )
    transmission_type = models.ForeignKey(
        TransmissionType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="transmission_type",
    )
    price = models.FloatField(_("Price"), help_text=_("Enter price"))
    year = models.CharField(
        _("Year"),
        max_length=4,
        help_text=_("Enter car manufactured year"),
        default=_("Year")
    )

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.car_model}"

    def display_car_maker(self):
        return f"{self.car_model.maker}"
        
    def display_car_model(self):
        return f"{self.car_model.model}"

    display_car_maker.short_description = _("Make")
    display_car_model.short_description = _("Model")
