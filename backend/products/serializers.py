from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(method_name='get_my_discount')
    
    class Meta:
        model = product
        # fields = ['title','description','price','get_discount','sale_price']
        fields = ['title','description','price','my_discount','sale_price']

    def get_my_discount(self, obj):
        return obj.get_discount()
        
        