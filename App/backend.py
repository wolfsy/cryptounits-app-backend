from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed

from .models import User
from .serializers import UserSerializer

class NewBackend(ModelBackend):
    def authenticate(request, user) -> User:
        
        if not user:
            raise AuthenticationFailed('Could not find the user!')

        if not check_password(request.data['UserPassword'], user.UserPassword):
            raise AuthenticationFailed('The wrong password has been provided!')
            
        serializer = UserSerializer(user)

        return serializer.data