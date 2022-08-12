from django.db import models

from user.models import User as UserModel


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    register_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
    
class Subscribe(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    buy_date = models.DateField(auto_now_add=True)
    start_subscribe = models.DateField(auto_now_add=True)
    end_subscribe = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} -> {self.product} : {self.start_subscribe}"