"""
URL configuration for SchocoBites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views 
from rest_framework.authtoken.views import obtain_auth_token
from main_app.views import UserLoginView, logout_view, TokenRefresh
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'Product')
router.register(r'orders', views.OrderView, 'Order')
router.register(r'reviews', views.ReviewView, 'Review')
router.register(r'users', views.UserViewSet, 'user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', views.CreateUserView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('main_app.urls')),
    path('api/login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefresh.as_view(), name='token_refresh'),
    path('logout/', logout_view, name='logout'),
]
