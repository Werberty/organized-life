from django.contrib.auth import get_user_model
from rest_framework import serializers
from organizer.models import Card, Tasks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user