from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ProfileListAPIView.as_view(), name='profile-list'),
    path('<int:pk>', ProfileDetailAPIView.as_view(), name='profile-list'),
    path('sign_up/', RegistrationAPIView.as_view(), name='sign-up'),
    path('sign_in/', LoginAPIView.as_view(), name='sign-in'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))

]
