from . import views
from django.urls import path
from .views import home, storeapp, product_list, view_cart, add_to_cart
from .views import about_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('store/', storeapp, name='storeapp'),
    path('products/', product_list, name='product_list'),
    path('view_cart/', view_cart, name='view_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('card_form/', views.card_data_view, name='card_form'),
    path('about.html/', about_view, name='about_view'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]









