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

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("название должно быть не менее 3 символов")
        return value

    def validate(self, attrs):
        name = attrs.get("name", "")
        description = attrs.get("description", "")

        if len(description) < 10:
            raise serializers.ValidationError({
                "description": "описание должно быть не менее 10 символов"
            })

        if name and description and name.lower() in description.lower():
            raise serializers.ValidationError({
                "description": "описание не должно содержать название продукта"
            })

        return attrs


def validar_price(value):
    if value < 0:
        raise serializers.ValidationError("цена должна быть неотрицательной")
    return value


def validar_category(value):
    if not Category.objects.filter(id=value.id).exists():
        raise serializers.ValidationError("категория не существует")
    return value


