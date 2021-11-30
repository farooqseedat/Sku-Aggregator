from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from drfAssignment.permissions import IsAdminUser, IsLoggedInUserOrAdmin
from products.models import Product
from products.serializers import ProductSerializer
from  products.filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['$name']
    filterset_class = ProductFilter

    def create(self, request, *args, **kwargs):
        if Product.objects.filter(product_hash=request.data.get("product_hash")).exists():
            product = Product.objects.get(product_hash=request.data.get("product_hash"))
            kwargs["partial"] = True
            self.kwargs["pk"] = product.id
            return self.update(request, *args, **kwargs)
        else:
            return super().create(request, *args, **kwargs)
    
    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            return super().get_permissions()
        return [permission() for permission in permission_classes]
