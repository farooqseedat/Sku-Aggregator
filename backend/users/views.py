from django.contrib.auth import authenticate
from rest_framework import viewsets 
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import token_refresh
from rest_framework_simplejwt.tokens import RefreshToken

from drfAssignment.permissions import IsAdminUser, IsLoggedInUserOrAdmin
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'], url_name='login')
    def login (self, request, *args, **kwargs):
        if request.data.get('email') and request.data.get('password'):
            user = authenticate(
                        email=request.data.get('email'),
                        password=request.data.get('password')
                    )
            if user:
                refresh = RefreshToken.for_user(user)
                res = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "name": user.first_name
                }
                return Response(res,status=status.HTTP_200_OK)
            
        return Response({"status":"Invalid email or password"},status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['POST'], url_path='token-refresh', url_name='token-refresh')
    def refresh_access_token(self, request, *args, **kwargs):
          return token_refresh(self.request._request,args,kwargs)

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', 'login', 'refresh_access_token']:
            permission_classes = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action in ['list', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            return super().get_permissions()
       
        return [permission() for permission in permission_classes]
