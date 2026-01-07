from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_view(request):

    if request.method == 'GET':
        instance=product.objects.all().order_by("?").first()
        data={}
        if instance:
            # data=model_to_dict(model_data)
            data=ProductSerializer(instance).data
        return Response(data)
    else:
        return Response({"message": "Hey Whatapp!"},status=200)
    
   