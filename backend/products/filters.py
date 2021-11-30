from django_filters import rest_framework as filters
from django.db.models import Q

from products.models import Product, ProductCategory


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    gender = filters.CharFilter(field_name='gender', lookup_expr='startswith')
    brands = filters.CharFilter(method='filter_brands', field_name='brands')
    categories = filters.CharFilter(method='filter_categories', field_name='category')

    def filter_brands(self, queryset, name, value):
        query = Q()
        for value in value.split(','):
            query = query | Q(brand=value)

        return queryset.filter(query)

    def filter_categories(self, queryset, name, value):
        query = Q()
        for value in value.split(','):
            query = query | Q(category__category__iexact=value)

        return queryset.filter(query)

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'categories', 'brands', 'gender']
