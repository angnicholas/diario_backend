from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomUserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        created_user = serializer.save()

        print(created_user, type(created_user))

        # if request.data['role'] == 'TN':
        #     #Create a new technician object tied to the user.
        #     Technician.objects.create(
        #         user=created_user,
        #         accepts_ot=False,
        #         technician_contact=Contact.objects.create(
        #             name=request.data['username'] #Temporarily store the guy's name as their username until they decide to change it?
        #         ),
        #     )

        return Response(serializer.data)