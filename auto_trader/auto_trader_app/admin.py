from django.contrib import admin
from .models import CarType, Maker, MakerModel, FuelType, TransmissionType, CarAd


class MakerModelAdmin(admin.ModelAdmin):
    list_display = ("maker", "model", "car_type")


class CarAdAdmin(admin.ModelAdmin):
    list_display = ("display_car_maker", "display_car_model", "year", "fuel_type", "transmission_type", "price")


admin.site.register(CarType)
admin.site.register(Maker)
admin.site.register(MakerModel, MakerModelAdmin)
admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(CarAd, CarAdAdmin)
