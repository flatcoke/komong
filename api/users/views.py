from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]
