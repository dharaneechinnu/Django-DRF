from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductmixinsView.as_view(),name='product-detail'),
    path('<int:pk>/delete',views.Deleteproductapiview.as_view(),name='product-delete'),
    path('<int:pk>/update',views.Updateproductapiview.as_view(),name='product-update'),
    path('',views.Createproductapiview.as_view(),name='product-create')
]
