from django.conf.urls.static import static
from django.urls import path

from ads import views
from first_django_1 import settings

urlpatterns = [
    path('', views.AdsListView.as_view()),
    path('<int:pk>/', views.AdsDetailView.as_view()),
    path('create/', views.AdsCreateView.as_view()),
    path('<int:pk>/update/', views.AdsPatchView.as_view()),
    path('<int:pk>/image/', views.AdsPatchImageView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
