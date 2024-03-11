import django_filters
from .models import Product, Warehouse

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['gte', 'lte'],
        }

class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = {
            'location': ['icontains'],
            'capacity': ['gte', 'lte'],
        }
