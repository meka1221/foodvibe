from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(User)
admin.site.register(Type)
admin.site.register(CategoryFood)
admin.site.register(Ingredient)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(MealPlan)


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ("title",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
