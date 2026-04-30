from django.db import models
from users.models import User
from products.models import Product
# Create your models here.
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ( (LIVE, 'Live'), (DELETE, 'Delete') )
    CART_STAGES = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELLIVERD = 3
    ORDER_REJECTED = 4
    ORDER_CHOICES = ((ORDER_PROCESSED,"ORDER_PROCESSED"),
                     (ORDER_DELLIVERD,"ORDER_DELLIVERD"),
                     (ORDER_REJECTED,"ORDER_REJECTED")
                     )
    order_status = models.IntegerField(choices=ORDER_CHOICES, default=CART_STAGES)


    owner =models.ForeignKey(User,on_delete=models.SET_NULL,related_name='orders',)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OrderItem(models.Model):
    product= models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts')
    quantity =models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items',)
    
