from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateField
from django.conf import settings

from store.settings import DEFAULT_AUTO_FIELD

# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=120)
    images = models.ImageField()
    desc = models.TextField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    created = models.DateField()

    def __str__(self) -> str:
        return self.name
class Customers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    mobile = models.CharField(max_length=12)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()

class orders(models.Model):
    user = models.ForeignKey(Customers,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_status = (
        ('1','pending'),
        ('2','accepted'),
        ('3','packed'),
        ('4','dispatched'),
        ('5','out for delivery'),
        ('7','delivered'),
        ('8','completed')
    )
    status = models.CharField(default='pending',choices = order_status,max_length=100 )