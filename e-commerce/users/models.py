from django.db import models
from products import product

# Create your models here.
class User(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ( (LIVE, 'Live'), (DELETE, 'Delete') )
    name = models.CharField(max_length=255)
    address = models.TextField()
    user = models.OneToOneField(US)
    password = models.CharField(max_length=255)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name