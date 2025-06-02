from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Модель пользователя
class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)  # Биография пользователя
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Аватар
    date_joined = models.DateTimeField(auto_now_add=True)  # Дата регистрации

    def __str__(self):
        return self.username


# Категория рецепта (можно несколько к одному рецепту)
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CategoryFood(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель ингредиента
class Ingredient(models.Model):
    name = models.CharField(max_length=255)  # Название ингредиента
    category = models.ForeignKey(CategoryFood, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


# Модель рецепта
class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Название рецепта
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор рецепта
    description = models.TextField()  # Краткое описание рецепта
    prep_time = models.IntegerField()  # Время приготовления в минутах
    difficulty = models.CharField(max_length=50,
                                  choices=[('easy', 'Легко'), ('medium', 'Средне'), ('hard', 'Трудно')])  # Сложность
    image = models.ImageField(upload_to='recipes/')  # Главное изображение рецепта
    category = models.ForeignKey(CategoryFood, on_delete=models.CASCADE) # Категория рецепта например: "Завтрак","Ужин","Десерт"
    published_at = models.DateTimeField(auto_now_add=True)  # Дата публикации
    servings = models.IntegerField()  # Количество порций
    ingredients = models.TextField()
    steps = models.TextField()  # Шаги приготовления
    is_featured = models.BooleanField(default=False)  # Флаг избранного рецепта

    # Параметры состава
    calories = models.IntegerField(default=0)  # Калории на порцию
    protein = models.FloatField(default=0)  # Белки в граммах
    fat = models.FloatField(default=0)  # Жиры в граммах
    carbohydrates = models.FloatField(default=0)  # Углеводы в граммах
    vitamins = models.TextField(null=True,
                                blank=True)  # Витамины, строка в формате: "Витамин C - 10 мг, Витамин B12 - 2 мкг"
    minerals = models.TextField(null=True, blank=True)  # Минералы, строка в формате: "Кальций - 200 мг, Железо - 5 мг"

    def __str__(self):
        return self.title


# Модель избранного
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Связь с рецептом
    added_at = models.DateTimeField(auto_now_add=True)  # Дата добавления в избранное

    class Meta:
        unique_together = ('user', 'recipe')  # Уникальность пары пользователь-рецепт


CHOICES_STAR = (
    (1, '1 звезда'),
    (2, '2 звезды'),
    (3, '3 звезды'),
    (4, '4 звезды'),
    (5, '5 звезд'),
)


# Модель комментария
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Связь с рецептом
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания комментария
    rating = models.IntegerField(choices=CHOICES_STAR)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Комментарий от {self.user.username} к рецепту {self.recipe.title}"


# План питания (например, план на 7 дней для похудения)
class MealPlan(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, related_name='meal_plans')
    duration_days = models.IntegerField(default=30)
    goal = models.CharField(max_length=100, choices=[
        ('loss', 'Похудение'),
        ('gain', 'Набор массы'),
        ('healthy', 'Здоровье')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

