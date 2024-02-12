from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsModerator, IsOwner
from users.serializers import UserCreateSerializer, UserSerializer


class UsersCreateView(generics.CreateAPIView):
    """Контроллер создания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UsersListView(generics.ListAPIView):
    """Котроллер списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsModerator]


class UsersDetailView(generics.RetrieveAPIView):
    """Котроллер описания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersUpdateView(generics.UpdateAPIView):
    """Контроллер обновления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersDeleteView(generics.DestroyAPIView):
    """Контроллер удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


