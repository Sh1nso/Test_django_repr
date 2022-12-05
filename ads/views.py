import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from ads.models import Ads
from category.models import Category
from first_django_1 import settings
from user.models import User


def index(request):
    return JsonResponse({"status": "ok"}, safe=False, status=200)


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('-price').select_related('category', 'author_id')
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ads = [{'id': ad.id,
                'name': ad.name,
                'author_id': ad.author_id.first_name,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'image': ad.image.url,
                'category': ad.category.name
                } for ad in page_obj]

        return JsonResponse({'ads': ads,
                             'num_pages': paginator.num_pages,
                             'total': paginator.count},
                            safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'author_id', 'price', 'description', 'address', 'is_published', 'category']

    def post(self, request, *args, **kwargs) -> json:
        data = json.loads(request.body)
        if data['is_published'].lower() == 'true':
            data['is_published'] = True
        else:
            data['is_published'] = False
        ads = Ads.objects.create(name=data.get('name'),
                                 author_id=User.objects.get(pk=data.get('author_id')),
                                 price=data.get('price'),
                                 description=data.get('description'),
                                 image=data.get('image'),
                                 is_published=data.get('is_published'),
                                 category=Category.objects.get(pk=data.get('category')))
        return JsonResponse({"name": ads.name})


class AdsDetailView(DetailView):
    queryset = Ads.objects.select_related('category', 'author_id')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
            'id': self.get_object().id,
            'name': self.get_object().name,
            'author_id': self.get_object().author_id.first_name,
            'price': self.get_object().price,
            'description': self.get_object().description,
            'is_published': self.get_object().is_published,
            'image': self.get_object().image.url,
            'category': self.get_object().category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdsPatchView(UpdateView):
    model = Ads
    fields = ['name', 'author_id', 'price', 'description', 'image', 'is_published', 'category']

    def patch(self, request, *args, **kwargs) -> json:
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        if category_data['is_published'].lower() == 'true':
            category_data['is_published'] = True
        else:
            category_data['is_published'] = False

        self.object.name = category_data.get('name')
        self.object.author_id = User.objects.get(pk=category_data.get('author_id'))
        self.object.price = category_data.get('price')
        self.object.description = category_data.get('description')
        self.object.image = category_data.get('image')
        self.object.is_published = category_data.get('is_published')
        self.object.category = Category.objects.get(pk=category_data.get('category'))

        self.object.save()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name})


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


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> json:
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})

# def add_data(request):
#     f = open('dataset/ad.json', 'r', encoding='utf-8')
#     data = json.load(f)
#     for i in data:
#         # location = Location.objects.get(pk=i.get('location_id'))
#         # user = User(first_name=i.get('first_name'),
#         #             last_name=i.get('last_name'),
#         #             username=i.get('username'),
#         #             password=i.get('password'),
#         #             role=i.get('role'),
#         #             age=i.get('age'),
#         #             location_id=location)
#         # category = get_object_or_404(Category, pk=i.get('category_id'))
#         category = Category.objects.get(pk=i.get('category_id'))
#         author = User.objects.get(pk=i.get('author_id'))
#         ads = Ads(name=i.get('name'),
#                   author_id=author,
#                   price=i.get('price'),
#                   description=i.get('description'),
#                   image=i.get('image'),
#                   category=category
#                   )
#         if i.get('is_published') == 'TRUE':
#             ads.is_published = True
#         else:
#             ads.is_published = False
#         ads.save()
#     f.close()
#     return JsonResponse({'status': 'ok!'})
