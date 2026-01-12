from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    Owner = UserPublicSerializer(source='user', read_only=True)
    #my_discount = serializers.SerializerMethodField(method_name='get_my_discount')
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    edit_url = serializers.SerializerMethodField(read_only=True)
    #email = serializers.EmailField(write_only=True)
    title= serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title_validator])
    class Meta:
        model = Product
        # fields = ['title','description','price','get_discount','sale_price']
        fields = ['Owner','edit_url', 'url', 'pk', 'title', 'description', 'price', 'sale_price']

    def create(self, validated_data):
        email = validated_data.pop('email')
        print("Email:", email)
        obj = super().create(validated_data)
        return obj
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    
    


    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update",kwargs={'pk':obj.pk},request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return "Not Available"
        if not isinstance(obj, Product):
            return "Not Available in Instance"
        return obj.get_discount()
        
        