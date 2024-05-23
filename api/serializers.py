from rest_framework import serializers
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