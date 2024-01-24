from django.contrib import admin
from django.urls import path, include
from exchange.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchange/', include('exchange.urls')),
    path('', index, name='index'),
]
