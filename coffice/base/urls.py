from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('like/<str:pk>/', views.favorited_coffee_shop, name="favorited_coffee_shop"),
    path('room/', views.room, name="room"),
    path('logout/', views.logout, name='logout'),
    path('coffee_shop/<str:pk>/', views.coffee_shop_detail, name='coffee_shop_detail'),
    path('make/<str:cnpj>/', views.make_reservation, name='make_reservation'),
    path('my/', views.reservation_list, name='reservation_list'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('home/', views.home, name="home.html"),

]