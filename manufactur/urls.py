from django.urls import path
from .views import get_products, get_warehouses

urlpatterns = [
    path('products/', get_products),
    path('warehouses/', get_warehouses),
]
