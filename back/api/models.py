from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255,
                            default='https://restolife.kz/upload/information_system_6/2/2/1/item_22198/information_items_property_25471.jpg')
    address = models.CharField(max_length=100, default='Tole bi, 170')
    contact = models.CharField(max_length=100, default='+7 (707) 777 77 77')
    avg_cost = models.IntegerField(default=4500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='restaurants')

    def __str__(self):
        return '{}'.format(self.name)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=3000)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='meals')

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self):
        return '{}'.format(self.name)


class Review(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='reviews')

    def __str__(self):
        return '{}: {}'.format(self.user, self.restaurant)


class OrderManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Order(models.Model):
    meal_name = models.CharField(max_length=200)
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = OrderManager()

    def __str__(self):
        return '{}: {}'.format(self.meal_name, self.count)