from django.urls import path



from . import views
from .views import get_products, get_warehouses , ProductListView
urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('warehouses/', get_warehouses, name='get_warehouses'),
    path('',ProductListView.as_view()),


]


