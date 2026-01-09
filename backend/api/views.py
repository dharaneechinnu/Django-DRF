from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_view(request):

    serializer=ProductSerializer(data=request.data,many=True)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        return Response(serializer.data)
 
    return Response({"data":"No products available"})       
    
   