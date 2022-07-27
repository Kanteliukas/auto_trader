from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from .models import CarAd, Images
from .form import CreateAdForm, ImageForm
from .filters import CarAdFilter


def index(request):
    response = render(request, "index.html")
    return response


class CarAdsListView(generic.ListView):
    model = CarAd
    template_name = "car_ads_list.html"
    context_object_name = "car_ads_list"
    filterset_class = CarAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


class CarAdDetailView(generic.DetailView):
    model = CarAd
    template_name = "car_ad_detail.html"


def new_car_ad(request):

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == "POST":

        carAdForm = CreateAdForm(request.POST)
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
            messages.success(request, _("Success"))
            return HttpResponseRedirect("/auto_trader_app/carads")
        else:
            print(carAdForm.errors, formset.errors)
    else:
        carAdForm = CreateAdForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(
        request, "new_car_ad.html", {"carAdForm": carAdForm, "formset": formset}
    )
