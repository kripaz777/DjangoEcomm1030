# Serializers define the API representation.
from rest_framework import routers, serializers, viewsets
from .models import *
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name","category","brand","price","discounted_price","image","description","specification","slug","label","stock"]



