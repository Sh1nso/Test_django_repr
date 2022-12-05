import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from category.models import Category


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')
        return JsonResponse([{'id': category.id,
                              'name': category.name} for category in self.object_list],
                            safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs) -> json:
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.get_object().id,
            "name": self.get_object().name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs) -> json:
        data = json.loads(request.body)

        category = Category.objects.create(name=data.get('name'))

        return JsonResponse({'id': category.id,
                             'name': category.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryPatchView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs) -> json:
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data.get('name')

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> json:
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})
