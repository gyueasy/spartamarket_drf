from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer,
    ProductDetailSerializer,
)
from .models import Product


class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        Products = Product.objects.all()
        serializer = ProductSerializer(Products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductDetailSerializer(Product)
        return Response(serializer.data)

    def put(self, request, pk):
        Product = self.get_object(pk)
        product_data = request.data.copy()
        if 'image' not in request.data:
            product_data['image'] = Product.image
        serializer = ProductDetailSerializer(
            Product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
