from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import CarAd


def index(request):
    response = render(request, "index.html")
    return response

class CarAdsListView(generic.ListView):
    model = CarAd
    template_name = "car_ads_list.html"
    context_object_name = "car_ads_list"

    def get_queryset(self):
        return CarAd.objects.all()
