from django.urls import path
from .views import get_products, get_warehouses, ProductView

urlpatterns = [
    path('products/', get_products),
    path('warehouses/', get_warehouses),
    path('', ProductView.as_view()),

]
