from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer , OrderSerializer, ReviewSerializer, UserSerializer
from .models import Product , Order, Review
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return response

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        product = self.request.query_params.get('product')
        return Review.objects.filter(product_id=product)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# def home(request):
#     # Send a simple HTML response
#     return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# User Login (JWT Token Generation)
class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            "refresh": response.data["refresh"],
            "access": response.data["access"],
            "message": "Login successful!"
        })

# Refresh Access Token
class TokenRefresh(TokenRefreshView):
    permission_classes = [AllowAny]

# Logout User by Blacklisting Token
@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    try:
        token = request.data.get('refresh')
        if not token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
        from rest_framework_simplejwt.tokens import RefreshToken

        refresh_token = RefreshToken(token)
        refresh_token.blacklist()  # Blacklist the refresh token
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": "Invalid token or token expired"}, status=status.HTTP_400_BAD_REQUEST)

