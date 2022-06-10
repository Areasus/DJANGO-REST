from rest_framework import serializers
from .models import *

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields='__all__'

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields='__all__'