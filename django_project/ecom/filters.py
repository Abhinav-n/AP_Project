from .models import Product, Review
import django_filters
from django import forms
from model_utils import Choices


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'filters', 'price']
