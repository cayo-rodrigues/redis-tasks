from time import sleep

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from tasks.settings import CACHE_TTL


class TodosCacheFlowMixin:
    cache_key_prefix = "todos"

    @method_decorator(cache_page(CACHE_TTL, key_prefix=cache_key_prefix))
    def list(self, request, *args, **kwargs):
        sleep(3)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.delete_many(cache.keys(f"*{self.cache_key_prefix}*"))
        return response
