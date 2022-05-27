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
        }


    def create(self, validated_data):
        if not validated_data['is_admin']:
            is_admin = validated_data.pop('is_admin', None)
            user = User.objects.create_user(**validated_data)
            return user
        if validated_data['is_admin']:
            is_admin = validated_data.pop('is_admin', None)
            user = User.objects.create_superuser(**validated_data)
            return user
        return super().create(validated_data)
