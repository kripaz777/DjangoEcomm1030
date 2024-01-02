from django.shortcuts import render,redirect
from .views import *
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['sale_products'] = Product.objects.filter(label='sale')


class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['contact_info'] = ContactInfo.objects.all()
        self.views['hot_news'] = Product.objects.filter(label = 'hot')
        self.views['new_news'] = Product.objects.filter(label = 'new')


        return render(request,'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        self.views
        cat_id = Category.objects.get(slug = slug).id
        self.views['product_category'] = Product.objects.filter(category_id = cat_id)
        return render(request,'category.html',self.views)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views
        self.views['product_details'] = Product.objects.filter(slug = slug)
        cat_id = Product.objects.get(slug = slug).category_id
        self.views['related_products'] = Product.objects.filter(category_id = cat_id)
        return render(request,'product-detail.html',self.views)

class SearchView(BaseView):
    def get(self,request):
        self.views
        if request.method == 'GET':
            query = request.GET['query']
            if query == '':
                return redirect('/')
            self.views['search_products'] = Product.objects.filter(name__icontains = query)
        return render(request,'search.html',self.views)


def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                return redirect('/signup')
            elif User.objects.fikter(email = email).exists():
                return redirect('/signup')
            else:
                User.objects.create_user(
                    first_name = fname,
                    lastname = lname,
                    username = username,
                    email = email,
                    password = password
                ).save()

    return render(request, 'signup.html')
