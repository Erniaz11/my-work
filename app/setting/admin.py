from django.contrib import admin
from app.setting.models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name", "description")
    inlines = [ProductImageInline]
    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "description", "category", "price")
        }),
        ("Дополнительно", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )
    readonly_fields = ("created_at",)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "image")
    list_filter = ("product",)
    search_fields = ("product__name",)
