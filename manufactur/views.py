from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Warehouse, ProductMaterial
from manufactur.serializer import ProductSerializer, WarehouseSerializer, ProductMaterialSerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_warehouses(request):
    warehouses = Warehouse.objects.all()
    serializer = WarehouseSerializer(warehouses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_materials(request, product_id):
    product_materials = ProductMaterial.objects.filter(product_id=product_id)
    serializer = ProductMaterialSerializer(product_materials, many=True)
    return Response(serializer.data)