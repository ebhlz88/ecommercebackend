from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import product
from .serializers import ProductSerilizer

from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.decorators import api_view;
from rest_framework.decorators import parser_classes

class allproducts(APIView):
    
    def get(self, request, format=None):
        allproducts = product.objects.all()
        title = request.query_params.get('productname', None)
        if title is not None:
            allproducts = product.filter(title__icontains=title)
        product_serializer = ProductSerilizer(allproducts, many=True)
        return Response(product_serializer.data)

    parser_classes = [FormParser,MultiPartParser]
    def post(self, request,format=None):   
        products_serializer = ProductSerilizer(data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        