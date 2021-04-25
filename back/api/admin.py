from django.contrib import admin
from api.models import Category, Restaurant, Fastfood, Cafe, RestaurantMeal, CafeMeal, FastfoodMeal, Order,\
                       RestaurantReview, CafeReview, FastfoodReview


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'avg_cost', 'category', 'image_url', 'info')


@admin.register(Fastfood)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'avg_cost', 'category', 'image_url',  'info')


@admin.register(Cafe)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'avg_cost', 'category', 'image_url',  'info')


@admin.register(RestaurantMeal)
class RestaurantMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'structure', 'time', 'place',)


@admin.register(CafeMeal)
class CafeMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'structure', 'time', 'place',)


@admin.register(FastfoodMeal)
class FastfoodMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'structure', 'time', 'place',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal_name', 'count', 'structure', 'time', 'user',)


@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'place',)


@admin.register(CafeReview)
class CafeReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'place',)


@admin.register(FastfoodReview)
class FastfoodReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'place',)

