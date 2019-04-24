from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, validators=[])
    email = serializers.EmailField(required=True, validators=[])
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    email_without_domain = serializers.SerializerMethodField(read_only=True)

    validate_password = make_password

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'password',
                  'email_without_domain', 'is_kmong_email',)

    @staticmethod
    def get_email_without_domain(obj):
        try:
            return obj.email.split('@')[0]
        except AttributeError:
            return ''
