from django.urls import include, path
from .views import CustomTokenObtainPairView, CustomUserCreateView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('jwt/login', CustomTokenObtainPairView.as_view()),
    path('register', CustomUserCreateView.as_view()),
]