from djoser.serializers import UserCreateSerializer as BaseuserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseuserCreateSerializer):
    class Meta(BaseuserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']
