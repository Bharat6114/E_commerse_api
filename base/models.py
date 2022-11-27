from itertools import product
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL, null =True)
    name  = models.CharField(max_length=200 ,null=True,blank =True)
    image = models.ImageField(upload_to ='products',null=True,blank=True)
    brand =models.CharField(max_length=200,null=True,blank =True)
    category =models.CharField(max_length=200,null=True,blank =True)
    desscription =models.TextField( null=True,blank=True)
    rating =models.DecimalField(max_digits=7,decimal_places=2)
    numreview =models.IntegerField(null=True,blank=True,default=0)
    price =models.DecimalField(max_digits=7,decimal_places=2,null=True)
    countinstock =models.IntegerField(null=True,blank=True,default=0)
    create_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Reviews(models.Model):
    product =models.ForeignKey(Product,on_delete=models.SET_NULL, null =True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL, null =True)
    name  = models.CharField(max_length=200 ,null=True,blank =True)
    rating =models.DecimalField(max_digits=7,decimal_places=2)
    comment =models.TextField( null=True,blank=True)
    create_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.rating)
class Order(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL, null =True)
    paymentMethod = models.CharField(max_length=200,null=True,blank=True)
    taxprice =models.DecimalField(max_digits=7,decimal_places=2)
    shippingPrice =models.DecimalField(max_digits=7,decimal_places=2)
    isPaid =models.BooleanField(default=False)
    isDelivered =models.BooleanField(default=False)
    deliveredAt =models.DateTimeField(auto_now_add=False)
    createdAt =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.createdAt)
class OrderItem(models.Model):
    product =models.ForeignKey(Product,on_delete=models.SET_NULL, null =True)
    order =models.ForeignKey(Order,on_delete=models.SET_NULL, null =True)
    name =models.CharField(max_length=200 ,null=True,blank =True)
    qut =models.DecimalField(max_digits=7,decimal_places=2)
    price =models.DecimalField(max_digits=7,decimal_places=2)
    #image =
    def __str__(self):
        return str(self.name)
class ShipingAddress(models.Model):
    order =models.ForeignKey(Order,on_delete=models.CASCADE, null =True)
    address =models.CharField(max_length=200 ,null=True,blank =True)
    city =models.CharField(max_length=200 ,null=True,blank =True)
    postalCode =models.CharField(max_length=200 ,null=True,blank =True)
    countary =models.CharField(max_length=200 ,null=True,blank =True)
    shipping_price =models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return str(self.order)

