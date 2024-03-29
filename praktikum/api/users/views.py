from django.forms import model_to_dict
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.users.serializers import (
    RegisterSerializer, LoginSerializer, LoginResponseSerializer
)
from api.users.service.auth import Authenticator
from api.users.service.regiter import Registerer


class AuthViewSet(ViewSet):
    """ViewSet авторизации/регистрации пользователей."""

    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={
            status.HTTP_200_OK: 'success',
        }
    )
    @action(methods=('post',), detail=False)
    def register(self, request):
        """Эндпоинт на регистрацию пользователя."""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Registerer.register(serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={status.HTTP_200_OK: LoginResponseSerializer()}
    )
    @action(methods=('post',), detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = Authenticator.login(
            serializer.validated_data.get('username'),
            serializer.validated_data.get('password'),
            request
        )
        serializer = LoginResponseSerializer(
            data=dict(token=token, user=model_to_dict(user))
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
