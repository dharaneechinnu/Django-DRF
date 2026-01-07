from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import product
def api_view(request):
  
    model_data=product.objects.all().order_by("?").first()

    return JsonResponse(model_data)