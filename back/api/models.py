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
    info = models.CharField(max_length = 2000, default='The best place')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='restaurants')

    def __str__(self):
        return '{}'.format(self.name)


class Cafe(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255,
                            default='https://restolife.kz/upload/information_system_6/2/2/1/item_22198/information_items_property_25471.jpg')
    address = models.CharField(max_length=100, default='Abay, 170')
    contact = models.CharField(max_length=100, default='+7 (707) 777 77 77')
    avg_cost = models.IntegerField(default=4500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='cafes')
    info = models.CharField(max_length = 2000, default='The best place')
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Cafe'
        verbose_name_plural = 'Cafes'


class Fastfood(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255,
                            default='https://restolife.kz/upload/information_system_6/2/2/1/item_22198/information_items_property_25471.jpg')
    address = models.CharField(max_length=100, default='Abay, 170')
    contact = models.CharField(max_length=100, default='+7 (707) 777 77 77')
    avg_cost = models.IntegerField(default=4500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='fastfoods')
    info = models.CharField(max_length = 2000, default='The best place')
    def __str__(self):
        return '{}'.format(self.name)


class RestaurantMeal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=3000)
    structure = models.CharField(max_length=3000, default='Cheese, Milk, Sugar, Salt')
    time = models.CharField(max_length=200, default='30 minutes')
    place = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='restaurantmeals')

    class Meta:
        verbose_name = 'Restaurant Meal'
        verbose_name_plural = 'Restaurant Meals'

    def __str__(self):
        return '{}'.format(self.name)


class CafeMeal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=3000)
    structure = models.CharField(max_length=3000, default='Cheese, Milk, Sugar, Salt')
    time = models.CharField(max_length=200, default='30 minutes')
    place = models.ForeignKey(Cafe, on_delete=models.CASCADE,
                                   related_name='cafemeals')

    class Meta:
        verbose_name = 'Cafe Meal'
        verbose_name_plural = 'Cafe Meals'

    def __str__(self):
        return '{}'.format(self.name)


class FastfoodMeal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=3000)
    structure = models.CharField(max_length=3000, default='Cheese, Milk, Sugar, Salt')
    time = models.CharField(max_length=200, default='30 minutes')
    place = models.ForeignKey(Fastfood, on_delete=models.CASCADE,
                                   related_name='fastfoodmeals')

    class Meta:
        verbose_name = 'Fastfood Meal'
        verbose_name_plural = 'Fastfood Meals'

    def __str__(self):
        return '{}'.format(self.name)


class RestaurantReview(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='restaurantreviews')

    def __str__(self):
        return '{}: {}'.format(self.user, self.place)


class CafeReview(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Cafe, on_delete=models.CASCADE,
                                   related_name='cafereviews')

    def __str__(self):
        return '{}: {}'.format(self.user, self.place)


class FastfoodReview(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Fastfood, on_delete=models.CASCADE,
                                   related_name='fastfoodreviews')

    def __str__(self):
        return '{}: {}'.format(self.user, self.place)


class OrderManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Order(models.Model):
    meal_name = models.CharField(max_length=200)
    count = models.IntegerField()
    structure = models.CharField(max_length=300, default='Cheese, Milk, Sugar, Salt')
    time = models.CharField(max_length=200, default='30 minutes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = OrderManager()

    def __str__(self):
        return '{}: {}'.format(self.meal_name, self.count, self.structure, self.time, self.user)
