from django.shortcuts import render
from .views import *
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['contact_info'] = ContactInfo.objects.all()
        self.views['hot_news'] = Product.objects.filter(label = 'hot')
        self.views['new_news'] = Product.objects.filter(label = 'new')


        return render(request,'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['product_category'] = Product.objects.filter(category_id = cat_id)
        return render(request,'category.html',self.views)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views['product_details'] = Product.objects.filter(slug = slug)
        return render(request,'product-detail.html',self.views)
