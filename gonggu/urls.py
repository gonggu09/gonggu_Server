from django.urls import path, include
from .views import ItemViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'item', ItemViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]