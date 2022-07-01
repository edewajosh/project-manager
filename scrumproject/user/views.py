from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer, UserPermissionsSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'update' or 'partial_update':
            return UserPermissionsSerializer
        return self.serializer_class

