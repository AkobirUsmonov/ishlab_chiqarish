from rest_framework import serializers
from .models import Product, Warehouse, Material


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
serializer = ProductSerializer(Product, many=True)

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
serializer = WarehouseSerializer(Warehouse, many = True)

class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
serializer = ProductMaterialSerializer(Warehouse, many = True)

