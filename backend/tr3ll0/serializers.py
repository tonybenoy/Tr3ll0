from rest_framework import serializers
from .models import Category, Items


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "category_name")


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ("id", "item", "itemtitle", "category_id")
