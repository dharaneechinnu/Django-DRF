from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['title','description','price','get_discount','sale_price']
        