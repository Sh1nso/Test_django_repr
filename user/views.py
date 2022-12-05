import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from first_django_1 import settings
from location.models import Location
from user.models import User


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        user_qs = User.objects.annotate(total_ads=Count('ads'))
        self.object_list = self.object_list.order_by('username').select_related('location_id')
        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        users = [{'id': user.id,
                  'first_name': user.first_name,
                  'last_name': user.last_name,
                  'username': user.username,
                  'role': user.role,
                  'age': user.age,
                  'locations': user.location_id.name,
                  'total_ads': user.total_ads} for user in page_obj]

        return JsonResponse({'users': users,
                             'num_pages': paginator.num_pages,
                             'total': paginator.count},
                            safe=False)


class UserDetailView(DetailView):
    queryset = User.objects.select_related('location_id')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        user_qs = User.objects.annotate(total_ads=Count('author_id'))

        return JsonResponse({
            'id': self.get_object().id,
            'first_name': self.get_object().first_name,
            'last_name': self.get_object().last_name,
            'username': self.get_object().username,
            'role': self.get_object().role,
            'age': self.get_object().age,
            'locations': self.get_object().location_id.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']

    def post(self, request, *args, **kwargs) -> json:
        data = json.loads(request.body)

        ads = User()
        ads.first_name = data.get('first_name')
        ads.last_name = data.get('last_name')
        ads.username = data.get('username')
        ads.password = data.get('password')
        ads.role = data.get('role')
        ads.age = data.get('age')
        location = Location.objects.get_or_create(name=data.get('locations'))
        ads.location_id = location[0]
        ads.save()
        return JsonResponse({"name": ads.first_name})


@method_decorator(csrf_exempt, name='dispatch')
class UserPatchView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location_id']

    def patch(self, request, *args, **kwargs) -> json:
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.first_name = user_data.get('first_name')
        self.object.last_name = user_data.get('last_name')
        self.object.username = user_data.get('username')
        self.object.password = user_data.get('password')
        self.object.role = user_data.get('role')
        self.object.age = user_data.get('age')
        location = Location.objects.get_or_create(name=user_data.get('locations'))
        self.object.location_id = location[0]

        self.object.save()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.first_name})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> json:
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})
