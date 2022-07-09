from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class AppObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['isAdmin'] = user.is_superuser

        return token


class AppObtainPairView(TokenObtainPairView):
    serializer_class = AppObtainPairSerializer
