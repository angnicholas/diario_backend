from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer
from .permissions import IsTherapist


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomUserCreateView(APIView):
    permission_classes = [IsTherapist]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_user = serializer.save()
        print(created_user, type(created_user))
        return Response(serializer.data)
