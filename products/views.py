from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from categories.models import Category
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsManager

from django.shortcuts import get_object_or_404


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset         = Product.objects.all()


    def perform_create(self, serializer:ProductSerializer) -> None:
        category_id = self.request.data["category"]
        category = get_object_or_404(Category,id=category_id)
        serializer.save(account_id=self.request.user.id, 
                        category=category)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsManager]
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
        