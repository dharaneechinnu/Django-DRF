from rest_framework import generics

from . models import product
from .serializers import ProductSerializer
class ProductDetailsApiView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class Createproductapiview(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None

        if description is None:
            description = title
        serializer.save(description=description)

