from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.cache import cache
from django.test import TestCase, override_settings

from app.setting.models import Category
from app.setting.cache_utils import CATEGORY_LIST_CACHE_KEY


@override_settings(
    CACHES={
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "test-cache",
        }
    }
)
class CategoryCacheTests(TestCase):
    def test_category_list_cache_is_cleared_on_create(self):
        cache.delete(CATEGORY_LIST_CACHE_KEY)
        cache.set(CATEGORY_LIST_CACHE_KEY, {"cached": True}, 60)

        Category.objects.create(
            name="Новая категория",
            image=SimpleUploadedFile("category.jpg", b"fake-image", content_type="image/jpeg"),
        )

        self.assertIsNone(cache.get(CATEGORY_LIST_CACHE_KEY))
