from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('categories/', views.categories_view),
    path('categories/<int:pk>/', views.category_view),
    path('categories/<int:pk>/restaurants/', views.Restaurants.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantView.as_view()),
    path('restaurants/<int:pk>/meals/', views.Meals.as_view()),
    path('meals/<int:pk>/', views.MealView.as_view()),
    path('restaurants/<int:pk>/reviews/', views.Reviews.as_view()),
    path('orders/', views.Orders.as_view()),
    path('orders/<int:pk>/', views.OrderView.as_view()),
    path('clear/', views.Clearer.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', csrf_exempt(views.Register.as_view())),
]