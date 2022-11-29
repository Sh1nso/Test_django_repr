import json

from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Category


def index(request):
    return JsonResponse({"status": "ok"}, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        all_ads = Ads.objects.all()
        response = []
        for ads in all_ads:
            response.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        ads = Ads()

        ads.name = data.get("name")
        ads.author = data.get("author")
        ads.price = data.get("price")
        ads.description = data.get("description")
        ads.address = data.get("address")
        ads.is_published = data.get("is_published")
        ads.save()
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({

                "name": category.name
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        category = Category()

        category.id = data.get("id")
        category.name = data.get("name")
        category.save()
        return JsonResponse({"status": "ok"})


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.get_object().id,
            "name": self.get_object().name,
            "author": self.get_object().author,
            "price": self.get_object().price,
            "description": self.get_object().description,
            "address": self.get_object().address,
            "is_published": self.get_object().is_published
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.get_object().id,
            "name": self.get_object().name,
        })
