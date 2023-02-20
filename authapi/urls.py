from django.urls import include, path
from .views import (
    CustomTokenObtainPairViewPatient, 
    CustomTokenObtainPairViewTherapist, 
    CustomUserCreateView
)

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('jwt/patientlogin', CustomTokenObtainPairViewPatient.as_view()),
    path('jwt/therapistlogin', CustomTokenObtainPairViewTherapist.as_view()),
    path('register', CustomUserCreateView.as_view()),
]
