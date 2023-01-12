from rest_framework import generics
from .serializers import ProductSerializer, ProductPostSerializer
from .models import Product
from categories.models import Category
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsMethodGet, IsManager

class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset         = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            
            return ProductPostSerializer
        return ProductSerializer

    def perform_create(self, serializer:ProductSerializer) -> None:
        category = self.request.data["category"]
        
        serializer.save(account_id=self.request.user, category=category)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsManager]
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
        