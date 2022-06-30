from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer, AdminUserSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.path == '/api/v1/users/admin/':
            print('Here')
            return AdminUserSerializer
        return self.serializer_class

