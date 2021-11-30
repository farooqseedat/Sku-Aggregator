from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model


class UserAuthBackend(BaseBackend):
   
    def authenticate(self, request, email=None, password=None):
        User = get_user_model() 
        try:
            user = User.objects.get(email=email)
            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None 

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
