from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import CarAd, Images
from .form import CreateAdForm, NewCreateAdForm, ImageForm


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


def new_car_ad(request):

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == "POST":

        carAdForm = NewCreateAdForm(request.POST)
        formset = ImageFormSet(
            request.POST, request.FILES, queryset=Images.objects.none()
        )

        if carAdForm.is_valid() and formset.is_valid():
            car_ad_form = carAdForm.save(commit=False)
            car_ad_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form["image"]
                    photo = Images(car_ad=car_ad_form, image=image)
                    photo.save()
            messages.success(
                request,
            )
            return HttpResponseRedirect("/auto_trader_app/carads")
        else:
            print(carAdForm.errors, formset.errors)
    else:
        carAdForm = NewCreateAdForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(
        request, "new_car_ad.html", {"carAdForm": carAdForm, "formset": formset}
    )
