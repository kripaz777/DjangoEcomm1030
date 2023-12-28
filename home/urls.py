from django.urls import path,include
from .views import *
urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('category/<slug>', CategoryView.as_view(), name='category'),
path('details/<slug>', ProductDetailView.as_view(), name='details'),

]