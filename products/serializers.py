from rest_framework import serializers
from categories.serializers import CategorySerilizer
from .models import Product
from categories.models import Category
from django.shortcuts import get_object_or_404


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Product
        
        fields = [
            "id",
            "name",
            "description",
            "price",
            "amount",
            "category", 
            "account_id",
        ] 
        
        read_only_fields = ["id", "account_id"]
        depth = 1
        
    

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class ProductPostSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Product
        
        fields = [
            "id",
            "name",
            "description",
            "price",
            "amount",
            "category", 
            "account_id",
        ] 
        
        read_only_fields = ["id", "account_id"]
        
        
    def create(self, validated_data:dict)-> Product:
        categorie_id = validated_data.pop("category")
        categorie_obj = get_object_or_404(Category,pk=categorie_id)
        product = Product.objects.create(**validated_data)
        product.category = categorie_obj
        return product