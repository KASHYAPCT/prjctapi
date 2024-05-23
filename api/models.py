from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Detials(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Cars(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    # price=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name