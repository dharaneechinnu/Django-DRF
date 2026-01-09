from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(method_name='get_my_discount')
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        # fields = ['title','description','price','get_discount','sale_price']
        fields = ['url','pk','title','description','price','my_discount','sale_price']

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={'pk':obj.pk},request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return "Not Available"
        if not isinstance(obj, Product):
            return "Not Available in Instance"
        return obj.get_discount()
        
        