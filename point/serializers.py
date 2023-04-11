# from locale import ABDAY_1
from .views import *
from rest_framework import serializers
from .views import *


class NameSerializer (serializers.Serializer):
    name = serializers.CharField(max_length=200)


class DataSerializer (serializers.Serializer):
    v1 = serializers.DecimalField(max_digits=19, decimal_places=2)
    v2 = serializers.DecimalField(max_digits=19, decimal_places=2)
    v3 = serializers.DecimalField(max_digits=19, decimal_places=2)
    v4 = serializers.DecimalField(max_digits=19, decimal_places=2)
    v5 = serializers.DecimalField(max_digits=19, decimal_places=2)
    v6 = serializers.DecimalField(max_digits=10, decimal_places=2)
    v7 = serializers.DecimalField(max_digits=10, decimal_places=2)


 
    

