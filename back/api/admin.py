from django.contrib import admin
from api.models import Category, Restaurant, Meal, Order, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'avg_cost', 'category', 'image_url',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'restaurant',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal_name', 'count', 'user',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'restaurant',)

