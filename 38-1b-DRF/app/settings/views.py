from rest_framework.generics import ListAPIView, CreateAPIView,\
RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app.settings.models import Category, Product
from app.settings.serializers import CategorySerializers, ProductSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related(
        "product_images"
        ).select_related("category")
    serializer_class = ProductSerializer