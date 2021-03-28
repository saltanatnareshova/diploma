from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from api.models import Category, Restaurant, Meal, Review, Order
from api.serializers import CategorySerializer, RestaurantSerializer, \
                            MealSerializer, ReviewSerializer, OrderSerializer

from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)


class Restaurants(APIView):
    filter_backends = (filters.OrderingFilter,)
    ordering = ('name', )

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        restaurants = category.restaurants.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            category = get_object_or_404(Category, id=self.kwargs['pk'])
            serializer.save(category=category)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class RestaurantView(APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(instance=restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        return Response(status=204)


class Meals(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('price',)

    def get_queryset(self):
        return Meal.objects.filter(restaurant=self.kwargs['pk'])

    def perform_create(self, serializer):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        serializer.save(restaurant=restaurant)


class MealView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class Reviews(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(restaurant=self.kwargs['pk'])

    def perform_create(self, serializer):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        serializer.save(user=self.request.user, restaurant=restaurant)


class Orders(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class Clearer(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        Order.objects.filter(user=request.user).delete()
        return Response(status=204)
