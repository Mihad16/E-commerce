from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product, name='product'),
    path('product_details/', views.product_details, name='product_details'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
]