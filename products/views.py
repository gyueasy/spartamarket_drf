from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer,
    ProductDetailSerializer,
    LikeSerializer
)
from .models import Product, Like
from .filters import ProductFilter

# 페이지네이션 설정
class ProductPagination(PageNumberPagination):
    page_size = 10  # 페이지당 10개의 상품을 보여줌
    page_size_query_param = 'page_size'  # URL에서 페이지 크기를 조정 가능
    max_page_size = 100  # 최대 페이지 크기

class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get(self, request):
        products = Product.objects.all()
        filtered_products = ProductFilter(request.GET, queryset=products).qs
        serializer = ProductSerializer(filtered_products, many=True)
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
        product = self.get_object(pk)
        product_data = request.data.copy()
        if 'image' not in request.data or request.data['image'] == '':
            product_data['image'] = product.image
        serializer = ProductDetailSerializer(product, data=product_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeProductView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, productId):
        user = request.user
        product = get_object_or_404(Product, id=productId)

        if Like.objects.filter(user=user, product=product).exists():
            return Response({'error': '이미 좋아요를 눌렀습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, product=product)
        product.likes_count += 1
        product.save()

        return Response({'message': '게시글에 좋아요를 눌렀습니다.'}, status=status.HTTP_201_CREATED)

class UnlikeProductView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, productId):
        user = request.user
        product = get_object_or_404(Product, id=productId)

        like = Like.objects.filter(user=user, product=product).first()
        if not like:
            return Response({'error': '좋아요를 누르지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        product.likes_count -= 1
        product.save()

        return Response({'message': '게시글 좋아요가 취소되었습니다.'}, status=status.HTTP_204_NO_CONTENT)