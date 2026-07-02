from rest_framework import serializers

from app.settings.models import Category, Product, ProductImage

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name", "image"
        )

class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id", "image"
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializers(
        source="product_image",
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "id", "name", "description","price",
            "created_at", "images"
        )