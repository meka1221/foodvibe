from .models import Recipe
from modeltranslation.translator import TranslationOptions, register


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


