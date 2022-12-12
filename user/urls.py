from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from user.views import UserListView, UserDetailView, UserCreateView, UserPatchView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserPatchView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]
