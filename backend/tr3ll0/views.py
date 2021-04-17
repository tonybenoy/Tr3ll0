from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import viewsets
from .models import Category


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()