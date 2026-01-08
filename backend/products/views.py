from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from . models import product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
 
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


class Updateproductapiview(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title
            instance.save()

class Deleteproductapiview(generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

class ProductmixinsView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None

        if description is None:
            description = title
        serializer.save(description=description)






# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None):

    # if request.method == "GET":
    #     if pk is not None:
    #         instance = get_object_or_404(product,pk=pk)
    #         data = ProductSerializer(instance).data
    #         return Response(data)
        
    #     instance = product.objects.all()
    #     data = ProductSerializer(instance,many=True).data
    #     return Response(data)
    
    # if request.method == "POST":
        # serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     title = serializer.validated_data.get('title')
        #     description = serializer.validated_data.get('description') or None

        #     if description is None:
        #         description = title
        #     serializer.save(description=description)
        # return Response(serializer.data)