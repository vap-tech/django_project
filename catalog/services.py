from django.core.cache import cache
from catalog.models import Category
from django.conf import settings


def get_category():
    if settings.CACHE_ENABLE:
        return cache.get_or_set('category_list', Category.objects.all())
    else:
        return Category.objects.all()
