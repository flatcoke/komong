from rest_framework import serializers

from .models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, validators=[])
    email = serializers.EmailField(required=True, validators=[])
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'password')
