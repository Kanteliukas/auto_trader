from django.contrib import admin
from .models import CarType, Maker, MakerModel, FuelType, TransmissionType, CarAd

admin.site.register(CarType)
admin.site.register(Maker)
admin.site.register(MakerModel)
admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(CarAd)
