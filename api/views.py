from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from api import serializers
from api.models import User


class UserExistsView(generics.RetrieveAPIView):
    serializer_class = serializers.UserExistsSerializer

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(User, email=request.GET.get('email').lower())
        return Response(self.get_serializer(user).data)
