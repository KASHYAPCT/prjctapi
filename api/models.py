from django.db import models 
from django.contrib.auth.models import User
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    category=models.ForeignKey(Category,models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product=models.ForeignKey(Product,models.CASCADE)
    size=models.CharField(max_length=10)
    actualprice=models.DecimalField(max_digits=10,decimal_places=2)
    discountprice=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.size

    
class Detials(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Cars(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class CarVariant(models.Model):
    car=models.ForeignKey(Cars,models.CASCADE)
    fuel=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    
    
class BlackListedToken(models.Model): 
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("token", "user")
    