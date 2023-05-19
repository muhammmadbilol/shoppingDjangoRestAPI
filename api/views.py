from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Category, Product, Cart
from . import serializers

from rest_framework import generics

from .serializers import CartSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductModelSerializer


# cart list
class CartAddProductView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def put(self, request, *args, **kwargs):
        cart = self.get_object()
        product_ids = request.data.get('product_ids', [])
        products = Product.objects.filter(id__in=product_ids)
        cart.products.add(*products)
        cart.save()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
