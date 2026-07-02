from django.urls import path
from app.setting.views import CategoryAPIView, ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="category-list"),
    path("products/", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]
