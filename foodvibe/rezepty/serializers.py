from rest_framework import serializers
from .models import *


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CategoryFoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MealPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'

