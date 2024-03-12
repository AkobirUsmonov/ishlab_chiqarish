from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25 , verbose_name="name")
    code = models.CharField(max_length=25 , verbose_name="code")

class Material(models.Model):
    name = models.CharField(max_length=100)

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
