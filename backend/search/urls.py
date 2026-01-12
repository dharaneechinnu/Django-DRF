from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchListNewView.as_view(), name='search'),
]
