from . import views
from django.urls import path

from .views import home, storeapp, product_list, view_cart, add_to_cart, CartView
from .views import about_view
from django.contrib.auth import views as auth_views
from .views import blog_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import shop_view
from .views import checkout_view, order_confirmation_view

urlpatterns = [
    path('', home, name='home'),
    path('store/', storeapp, name='storeapp'),
    path('products/', product_list, name='product_list'),
    path('view_cart/', view_cart, name='view_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('card_form/', views.card_data_view, name='card_form'),
    path('about/', about_view, name='about_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html', next_page='home'), name='logout'),
    path('blog/', blog_view, name='blog_view'),
    path('shop/', views.shop_view, name='shop_view'),
    path('checkout/', checkout_view, name='checkout_view'),
    path('order_confirmation/', order_confirmation_view, name='order_confirmation'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('contact/', views.contact_view, name='contact'),
    path('home/', views.home_view, name='store_home'),

]






