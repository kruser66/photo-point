from django.urls import path
from django.views.decorators.cache import cache_page
from exchange.views import get_current_usd


urlpatterns = [
    path('get_current_usd/', cache_page(10)(get_current_usd), name='get_current_usd'),
]
