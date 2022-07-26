from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import CarAd
from .form import CreateAdForm


def index(request):
    response = render(request, "index.html")
    return response


class CarAdsListView(generic.ListView):
    model = CarAd
    template_name = "car_ads_list.html"
    context_object_name = "car_ads_list"

    def get_queryset(self):
        return CarAd.objects.all()


class CarAdDetailView(generic.DetailView):
    model = CarAd
    template_name = "car_ad_detail.html"


class CarAdCreateView(generic.CreateView):
    model = CarAd
    form_class = CreateAdForm
    success_url = reverse_lazy("car-ads")
    template_name = "new_car_ad.html"
