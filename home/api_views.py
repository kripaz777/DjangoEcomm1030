# ViewSets define the view behavior.
from rest_framework import routers, serializers, viewsets
from .models import *
from .serializers import *
from rest_framework import generics
import django_filters.rest_framework
from rest_framework import filters


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'stock','label','brand']
    search_fields = ['name', 'description']
    ordering_fields = ['name','price','discounted_price']

