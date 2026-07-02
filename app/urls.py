from django.urls import path

from app.setting.views import CategoryAPIView, ProductListAPIView

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
]