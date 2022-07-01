from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer, AdminUserSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

