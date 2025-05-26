from django_filters.rest_framework import FilterSet
from .models import Recipe


class RecipeFilter(FilterSet):
    class Meta:
        model = Recipe
        fields = {
            'difficulty': ['exact'],
        }