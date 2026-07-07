from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache

from app.setting.cache_utils import CATEGORY_LIST_CACHE_KEY


@receiver(post_save, sender="setting.Category")
def clear_category_list_cache(sender, **kwargs):
    cache.delete(CATEGORY_LIST_CACHE_KEY)


@receiver(post_delete, sender="setting.Category")
def clear_category_list_cache_on_delete(sender, **kwargs):
    cache.delete(CATEGORY_LIST_CACHE_KEY)


class Category(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="category",
        verbose_name="Фото"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name = "Категорий"

class Product(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name="product_category",
        verbose_name="Категория товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание"
    )
    price = models.CharField(
        max_length=25,
        verbose_name="Цена"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product",
        verbose_name="Фото продукта"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_image",
        verbose_name="Изображение продукта"
    )

    class Meta:
        verbose_name = "Изображение Продукт"
        verbose_name_plural = "Изображение Продукты"