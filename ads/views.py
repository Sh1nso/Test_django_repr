import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView, UpdateView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

from ads.models import Ads
from ads.serializers import AdsListViewSerializer, AdsCreateSerializer, AdsRetrieveSerializer, AdsUpdateSerializer, \
    AdsDestroySerializer
from category.models import Category
from user.models import User


def index(request):
    return JsonResponse({"status": "ok"}, safe=False, status=200)


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsListViewSerializer

    def get(self, request, *args, **kwargs):
        ads_data_cat = request.GET.get('cat', None)
        ads_data_text = request.GET.get('text', None)
        ads_data_location = request.GET.get('location', None)
        ads_data_price_from = request.GET.get('price_from', None)
        ads_data_price_to = request.GET.get('price_to', None)
        if ads_data_cat:
            self.queryset = self.queryset.filter(
                category=int(ads_data_cat)
            )
        if ads_data_text:
            self.queryset = self.queryset.filter(
                name__icontains=ads_data_text
            )
        if ads_data_location:
            self.queryset = self.queryset.filter(
                author_id__location_id__name__icontains=ads_data_location
            )
        if ads_data_price_from and ads_data_price_to:
            self.queryset = self.queryset.filter(
                price__gte=int(ads_data_price_from),
                price__lte=int(ads_data_price_to)
            )
        return super().get(request, *args, **kwargs)


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsRetrieveSerializer


class AdsPatchView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer


class AdsDeleteView(DeleteView):
    queryset = Ads.objects.all()
    serializer_class = AdsDestroySerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsPatchImageView(UpdateView):
    queryset = Ads.objects.select_related('category', 'author_id')
    fields = ['image']

    def post(self, request, *args, **kwargs) -> json:
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author_id.first_name,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'image': self.object.image.url,
            'category': self.object.category.name
        })
