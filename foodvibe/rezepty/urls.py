from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='recipe_list'),
    path('<int:pk>/', RecipeDetailViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='recipe_detail'),
    path('category/', CategoryFoodViewSet.as_view({'get': 'list',
                                    'post': 'create'}), name='category_list'),
    path('type/', TypeViewSet.as_view({'get': 'list',
                                    'post': 'create'}), name='type_list'),
    path('mealplan/', MealPlanListCreateViewSet.as_view({'get': 'list',
                                       'post': 'create'}), name='mealplan_list'),
    path('favorite/', FavoriteViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='favorite_list'),
    path('favorite/<int:pk>/', RecipeDetailViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='recipe_detail'),
    path('', RecipeViewSet.as_view({'get': 'list',
                                    'post': 'create'}), name='recipe_list'),
    path('comment/', CommentViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='comment_detail'),
]

