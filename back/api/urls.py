from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('categories/', views.categories_view),
    path('categories/<int:pk>/', views.category_view),

    path('restaurants/', views.Restaurants.as_view()),
    path('categories/cafes/', views.Cafes.as_view()),
    path('categories/fastfoods/', views.Fastfoods.as_view()),

    path('restaurants/<int:pk>/', views.RestaurantView.as_view()),
    path('cafes/<int:pk>/', views.CafeView.as_view()),
    path('fastfoods/<int:pk>/', views.FastfoodView.as_view()),

    path('restaurants/<int:pk>/meals/', views.RestaurantMeals.as_view()),
    path('cafes/<int:pk>/meals/', views.CafeMeals.as_view()),
    path('fastfoods/<int:pk>/meals/', views.FastfoodMeals.as_view()),

    path('meals/<int:pk>/', views.MealView.as_view()),

    path('restaurants/<int:pk>/reviews/', views.RestaurantReviews.as_view()),
    path('cafes/<int:pk>/reviews/', views.CafeReviews.as_view()),
    path('fastfoods/<int:pk>/reviews/', views.FastfoodReviews.as_view()),

    path('orders/', views.Orders.as_view()),
    path('orders/<int:pk>/', views.OrderView.as_view()),
    path('clear/', views.Clearer.as_view()),

    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', csrf_exempt(views.Register.as_view())),
]