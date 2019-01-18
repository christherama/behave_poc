from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import User


class UserExistsSerializer(ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('email',)
