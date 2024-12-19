from django.contrib.auth import authenticate, logout
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import update_session_auth_hash

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *


# Create your views here.
class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.only('id', 'username')
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.only('username', 'first_name', 'last_name', 'email', 'phone_number')
    serializer_class = ProfileDetailSerializer


class RegistrationAPIView(APIView):
    queryset = Profile.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    # Чтобы swagger показывал параметры
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'success': _(f'User {user.username} is created'),
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'success': _(f'User {user.username} is logged in'),
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({
            'error': _('Username or password is incorrect')
        }, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        username = request.user.username if request.user else "Anonymous"
        # Выход пользователя из системы
        logout(request)
        return Response({"success": _(f"User {username} successfully logged out.")},
                        status=status.HTTP_200_OK)


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.set_password(serializer.data.get('confirm_new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({
                    'success': 'Password changed successfully.'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


