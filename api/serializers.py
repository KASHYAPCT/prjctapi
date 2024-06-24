from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import*


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class Detialsserializer(serializers.ModelSerializer):
    class Meta:
        model=Detials
        fields='__all__'


class Carsserializer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields='__all__'
  

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductVariantserializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariant
        fields='__all__'

class CarsVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarVariant
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        user.save()
        Token.objects.create(user=user)
        return user


