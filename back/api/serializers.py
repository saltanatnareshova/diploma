from rest_framework import serializers
from api.models import Category, Restaurant, Cafe, Fastfood, RestaurantReview, CafeReview, FastfoodReview,\
                       RestaurantMeal, CafeMeal, FastfoodMeal, Order
from django.contrib.auth.models import User
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email', 'is_staff')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    encoder = BCryptSHA256PasswordHasher()

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())
        user = User.objects.create(password=hashed_password, **validated_data)
        user.save()
        return user


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    image_url = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    avg_cost = serializers.IntegerField(required=True)
    category = CategorySerializer(read_only=True)
    info = serializers.CharField(required=True)

    def create(self, validated_data):
        restaurant = Restaurant(**validated_data)
        restaurant.save()
        return restaurant

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CafeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    image_url = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    avg_cost = serializers.IntegerField(required=True)
    category = CategorySerializer(read_only=True)
    info = serializers.CharField(required=True)

    def create(self, validated_data):
        cafe = Cafe(**validated_data)
        cafe.save()
        return cafe

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class FastfoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    image_url = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    avg_cost = serializers.IntegerField(required=True)
    category = CategorySerializer(read_only=True)
    info = serializers.CharField(required=True)

    def create(self, validated_data):
        fastfood = Fastfood(**validated_data)
        fastfood.save()
        return fastfood

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RestaurantMealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    structure = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    place = RestaurantSerializer(read_only=True)

    class Meta:
        model = RestaurantMeal
        fields = '__all__'


class CafeMealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    structure = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    place = CafeSerializer(read_only=True)

    class Meta:
        model = CafeMeal
        fields = '__all__'


class FastfoodMealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    structure = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    place = FastfoodSerializer(read_only=True)

    class Meta:
        model = FastfoodMeal
        fields = '__all__'


class RestaurantReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    user = UserSerializer(read_only=True)
    place = RestaurantSerializer(read_only=True)

    class Meta:
        model = RestaurantReview
        fields = '__all__'


class CafeReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    user = UserSerializer(read_only=True)
    place = CafeSerializer(read_only=True)

    class Meta:
        model = CafeReview
        fields = '__all__'


class FastfoodReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True)
    user = UserSerializer(read_only=True)
    place = FastfoodSerializer(read_only=True)

    class Meta:
        model = FastfoodReview
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    meal_name = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    structure = serializers.CharField(required=True)
    time = serializers.CharField(required=True)
    user = UserSerializer(read_only=True)
    # place = serializers.CharField(required=True)

    class Meta:
        model = Order
        fields = '__all__'