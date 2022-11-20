from rest_framework import serializers
from .views import *

class CSVDataSerializer (serializers.Serializer):
    a1 = serializers.DecimalField(max_digits=19, decimal_places=0)
    a2 = serializers.DecimalField(max_digits=19, decimal_places=2)
    a3 = serializers.DecimalField(max_digits=19, decimal_places=2)
    a4 = serializers.DecimalField(max_digits=19, decimal_places=2)
    a5 = serializers.DecimalField(max_digits=19, decimal_places=2)