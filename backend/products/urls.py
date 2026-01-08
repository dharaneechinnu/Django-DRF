from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductDetailsApiView.as_view(),name='product-detail'),
    path('create/',views.Createproductapiview.as_view(),name='product-create')
]
