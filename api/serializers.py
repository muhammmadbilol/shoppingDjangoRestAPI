from rest_framework import serializers
from . import models
from .models import Cart


class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    images = ProductImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('request').FILES
        product = models.Product.objects.create(**validated_data)

        for image_data in images_data.values():
            models.ProductImage.objects.create(product=product, image=image_data)

        return product

    def update(self, instance, validated_data):
        images_data = self.context.get('request').FILES
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        for image_data in images_data.values():
            models.ProductImage.objects.create(product=instance, image=image_data)

        return instance

class CategoryModelSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'products']
