from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from api.models import Category, Restaurant, Cafe, Fastfood, RestaurantMeal, CafeMeal, FastfoodMeal, RestaurantReview, CafeReview, FastfoodReview, Order
from api.serializers import CategorySerializer, RestaurantSerializer, CafeSerializer, FastfoodSerializer, \
                            RestaurantMealSerializer, CafeMealSerializer, FastfoodMealSerializer, \
                            RestaurantReviewSerializer, CafeReviewSerializer, FastfoodReviewSerializer, OrderSerializer

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

    def get(self, request):
        # category = get_object_or_404(Category, pk=pk)
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            # category = get_object_or_404(Category, id=self.kwargs['pk'])
            serializer.save()
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

class Cafes(APIView):
    filter_backends = (filters.OrderingFilter,)
    ordering = ('name', )

    def get(self, request):
        # category = get_object_or_404(Category, pk=pk)
        cafes = Cafe.objects.all()
        serializer = CafeSerializer(cafes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CafeSerializer(data=request.data)
        if serializer.is_valid():
            # category = get_object_or_404(Category, id=self.kwargs['pk'])
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class CafeView(APIView):
    def get(self, request, pk):
        cafe = get_object_or_404(Cafe, pk=pk)
        serializer = CafeSerializer(cafe)
        return Response(serializer.data)

    def put(self, request, pk):
        cafe = get_object_or_404(Cafe, pk=pk)
        serializer = CafeSerializer(instance=cafe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        cafe = get_object_or_404(Cafe, pk=pk)
        cafe.delete()
        return Response(status=204)


class Fastfoods(APIView):
    filter_backends = (filters.OrderingFilter,)
    ordering = ('name', )

    def get(self, request):
        # category = get_object_or_404(Category, pk=pk)
        fastfoods = Fastfood.objects.all()
        serializer = RestaurantSerializer(fastfoods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FastfoodSerializer(data=request.data)
        if serializer.is_valid():
            # category = get_object_or_404(Category, id=self.kwargs['pk'])
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class FastfoodView(APIView):
    def get(self, request, pk):
        fastfood = get_object_or_404(Fastfood, pk=pk)
        serializer = FastfoodSerializer(fastfood)
        return Response(serializer.data)

    def put(self, request, pk):
        fastfood = get_object_or_404(Fastfood, pk=pk)
        serializer = FastfoodSerializer(instance=fastfood, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        fastfood = get_object_or_404(Fastfood, pk=pk)
        fastfood.delete()
        return Response(status=204)


class RestaurantMeals(generics.ListCreateAPIView):
    serializer_class = RestaurantMealSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('price',)

    def get_queryset(self):
        return RestaurantMeal.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        serializer.save(place=restaurant)


class CafeMeals(generics.ListCreateAPIView):
    serializer_class = CafeMealSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('price',)

    def get_queryset(self):
        return CafeMeal.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        cafe = get_object_or_404(Cafe, id=self.kwargs['pk'])
        serializer.save(place=cafe)

class FastfoodMeals(generics.ListCreateAPIView):
    serializer_class = FastfoodMealSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ('price',)

    def get_queryset(self):
        return FastfoodMeal.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        fastfood = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        serializer.save(place=fastfood)


class MealView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantMeal.objects.all()
    serializer_class = RestaurantMealSerializer


class RestaurantReviews(generics.ListCreateAPIView):
    serializer_class = RestaurantReviewSerializer

    def get_queryset(self):
        return RestaurantReview.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        place = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        serializer.save(user=self.request.user, place=place)


class CafeReviews(generics.ListCreateAPIView):
    serializer_class = CafeReviewSerializer

    def get_queryset(self):
        return CafeReview.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        place = get_object_or_404(Cafe, id=self.kwargs['pk'])
        serializer.save(user=self.request.user, place=place)


class FastfoodReviews(generics.ListCreateAPIView):
    serializer_class = FastfoodReviewSerializer

    def get_queryset(self):
        return FastfoodReview.objects.filter(place=self.kwargs['pk'])

    def perform_create(self, serializer):
        place = get_object_or_404(Cafe, id=self.kwargs['pk'])
        serializer.save(user=self.request.user, place=place)


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
