from rest_framework import serializers
from realtime_chat.models import User

class RegisterUserSerializer(serializers.Serializer):

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        model = User

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.Serializer):
    
    class Meta:
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        model = User
    

