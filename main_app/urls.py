from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.generics import RetrieveAPIView
from .views import ProductView, OrderView, ReviewView   # Ensure this import works

router = DefaultRouter()
router.register(r'products', ProductView, basename='product')
router.register(r'orders', OrderView, basename='order')
router.register(r'reviews', ReviewView, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    #path('products/<int:id>/', ProductView.as_view()),
]