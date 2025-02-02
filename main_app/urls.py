from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView  # Ensure this import works

router = DefaultRouter()
router.register(r'products', ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]