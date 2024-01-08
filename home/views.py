from django.shortcuts import render,redirect
from .views import *
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

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
        self.views['product_review'] = ProductReview.objects.filter(slug = slug)
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
                messages.error(request, "Username already taken!")
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already used!")
                return redirect('/signup')
            else:
                User.objects.create_user(
                    first_name = fname,
                    last_name = lname,
                    username = username,
                    email = email,
                    password = password
                ).save()
        else:
            messages.error(request, "Password does not match!")
            return redirect('/signup')
    return render(request, 'signup.html')

def product_review(request,slug):
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        rating = request.POST['rating']
        review = request.POST['review']
        ProductReview.objects.create(
            username = username,
            email = email,
            rating = rating,
            review = review,
            slug = slug
        ).save()
    return redirect(f'/details/{slug}')

def add_to_cart(request,slug):
    username = request.user.username
    price = Product.objects.get(slug = slug).price
    discountred_price = Product.objects.get(slug = slug).discounted_price
    if discountred_price > 0:
        original_price = discountred_price
    else:
        original_price = price

    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug).quantity
        quantity +=1
        total = original_price * quantity
        Cart.objects.filter(slug = slug, username = username,checkout = False).update(
            quantity = quantity +1,
            total = total
        )
    else:
        Cart.objects.create(
            username = username,
            slug = slug,
            item = Product.objects.filter(slug = slug)[0],
            total = original_price
        ).save()

    return redirect('/')


class CartView(BaseView):
    def get(self,request):
        username = request.user.username
        self.views['cart_view'] = Cart.objects.filter(username = username, checkout = False)
        return render(request,'cart.html',self.views)