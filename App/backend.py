from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed

from .models import User

class NewBackend(ModelBackend):
    def authenticate(request) -> User:

        user: User = User.objects.filter(UserEmail = request.data['UserEmail']).first()

        if not user:
            raise AuthenticationFailed('Could not find the user!')

        if not check_password(request.data['UserPassword'], user.UserPassword):
            raise AuthenticationFailed('The wrong password has been provided!')
            