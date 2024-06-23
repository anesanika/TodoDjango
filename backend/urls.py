from django.contrib import admin
from django.urls import path, include
from.views import UserCreateView, CurrentUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('users/', UserCreateView.as_view(), name="user-create"),
    path('users/me/', CurrentUserView.as_view(), name='profile'),
    path('login/', obtain_auth_token, name='LogIn'),
]
