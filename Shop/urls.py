from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path('dark/', views.dark, name='store-dark'),
    path('light/', views.light, name='store-light'),
    path('cart/', views.cart, name='store-cart'),
    path('user/', views.user, name='store-user'),
    path('register/', views.register, name='store-user'),
    path('login/', views.login, name='store-user'),
    path('checkout/', views.checkout, name='store-checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('place_order/', views.placeOrder, name='place_order')
]