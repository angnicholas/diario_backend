from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    get_custom_token_obtain_serializer, 
    UserCreateSerializer
)
from .permissions import IsTherapist
from .options import ROLE_PATIENT, ROLE_THERAPIST


class CustomTokenObtainPairViewPatient(TokenObtainPairView):
    serializer_class = get_custom_token_obtain_serializer(ROLE_PATIENT)


class CustomTokenObtainPairViewTherapist(TokenObtainPairView):
    serializer_class = get_custom_token_obtain_serializer(ROLE_THERAPIST)
    

class CustomUserCreateView(APIView):
    permission_classes = [IsTherapist]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_user = serializer.save()
        print(created_user, type(created_user))
        return Response(serializer.data)
