from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from app.setting.models import Category, Product
from app.setting.serializers import CategorySerializers, ProductSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
    ).select_related("category")
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
    ).select_related("category")
    serializer_class = ProductSerializer
    lookup_field = "pk"