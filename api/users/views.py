from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def create(self, *args, **kwargs):
        self.permission_classes = (AllowAny,)
        super(UserViewSet, self).create(*args, **kwargs)
