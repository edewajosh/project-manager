from rest_framework.serializers import ModelSerializer

from user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_admin', 'is_active', 'last_login', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'last_login': {'read_only': True},
            'is_active': {'read_only': True},
            'is_admin': {'read_only': True},
        }


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserPermissionsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_admin', 'is_active', 'last_login', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'last_login': {'read_only': True},
            'is_active': {'read_only': True},
            'is_admin': {'read_only': True},
        }


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
# Is a good design pattern to provide an endpoint for creating superusers?
class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_admin', 'is_active', 'last_login', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'last_login': {'read_only': True},
            'is_active': {'read_only': True},
            'is_admin': {'read_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)