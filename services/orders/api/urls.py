from django.urls import path
from .views import OrderViewSet


urlpatterns = [
    path('orders/', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]
