from rest_framework import serializers

from app.setting.models import Category, Product, ProductImage

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
                    "id", "name", "image"
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
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = (
            "id", "name", "description", "price",
            "category", "created_at", "images"
        )
        read_only_fields = ("created_at", "images")