from django.urls import path

from . import views
from .views import get_products, get_warehouses

urlpatterns = [
    path('products/', get_products),
    path('warehouses/', get_warehouses),
    # path('products/', views.product_list, name='product_list'),
]


