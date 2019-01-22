from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from api import serializers
from api.services import UserService, UserNotFoundException


class UserExistsView(generics.RetrieveAPIView):
    serializer_class = serializers.UserExistsSerializer
    user_service = UserService()

    def retrieve(self, request, *args, **kwargs):
        try:
            user = self.user_service.find(email=request.GET.get('email').lower())
        except UserNotFoundException:
            raise Http404()
        else:
            return Response(self.get_serializer(user).data)
