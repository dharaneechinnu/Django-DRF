from rest_framework import generics
from rest_framework import mixins
from . models import Product
from .serializers import ProductSerializer
from api.mixins import IsStaffEditorPermissionMixins

from api.permissions import IsStaffEditorPermission

from rest_framework import permissions


class ProductDetailsApiView(IsStaffEditorPermissionMixins,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Createproductapiview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
  
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None

        if description is None:
            description = title
        serializer.save(description=description)


class Updateproductapiview(IsStaffEditorPermissionMixins,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title
            instance.save()

class Deleteproductapiview(IsStaffEditorPermissionMixins,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

class ProductmixinsView(IsStaffEditorPermissionMixins,mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Product.objects.all()
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



