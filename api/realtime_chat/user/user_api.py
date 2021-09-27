from rest_framework.response import Response
from rest_framework.views import APIView
from realtime_chat.user.user_serializers import RegisterUserSerializer, UserSerializer
from rest_framework import generics, permissions
from realtime_chat.models.user import User


class RegisterUserAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        serializer.save(**self.request.data)


class ListUserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)