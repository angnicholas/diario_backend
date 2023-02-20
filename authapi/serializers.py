from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions


User = get_user_model()  # Retrieve custom user model


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'display_name', 'role',
                  'average_sentiment', 'latest_sentiment', 'last_update')

def get_custom_token_obtain_serializer(role_code):
    class InnerSerializer(TokenObtainPairSerializer):
        def validate(self, attrs):
            data = super().validate(attrs)
            data['role'] = self.user.role
            data['id'] = self.user.pk

            if data['role'] == role_code:
                return data
            raise exceptions.AuthenticationFailed(
                "User is not of the correct role."
            )
    return InnerSerializer