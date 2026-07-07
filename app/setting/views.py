from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.core.cache import cache

from app.setting.models import Category, Product
from app.setting.serializers import CategorySerializers, ProductSerializer
from app.setting.cache_utils import CATEGORY_LIST_CACHE_KEY


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request, *args, **kwargs):
        cached_data = cache.get(CATEGORY_LIST_CACHE_KEY)
        if cached_data is not None:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(CATEGORY_LIST_CACHE_KEY, data, 60 * 5)
        return Response(data)

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
    ).select_related("category")
    serializer_class = ProductSerializer
class ProductcreateAPIView(CreateAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
    ).select_related("category")
    serializer_class = ProductSerializer

def perfom_create(self, serializer):
    serializer.save()
    cache.delete('product_list')

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related(
        "product_image"
    ).select_related("category")
    serializer_class = ProductSerializer
    lookup_field = "pk"


    