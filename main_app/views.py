from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from django.http import HttpResponse
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# def home(request):
#     # Send a simple HTML response
#     return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')