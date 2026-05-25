from django.urls import path
from . import views


urlpatterns = [

    path('account/', views.show_account, name='account'),

    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
]