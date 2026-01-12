from rest_framework import generics
from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer
from . import client
from rest_framework.response import Response

class SearchListNewView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        tags = request.GET.get('tag')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=400)
        try:
            results = client.perform_Search(query, tags=tags)
            print("Search Results:", results)
            return Response(results)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        user=None
        if self.request.user.is_authenticated:
            user=self.request.user
        result = qs.search(query,user=user)
        return result
