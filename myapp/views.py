from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer
from accounts.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from accounts.forms import LoginForm
from django.contrib.auth.hashers import make_password
from cart1.cart import Cart

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('username')
            email = cleaned_data.get('email')
            password = make_password(cleaned_data.get('password1'))
            customer = Customer(name=name, email=email, password=password)
            customer.save() # Save new customer to database
            return redirect('/login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/main')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form data.')
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

def petshop(request):
    return render(request, 'petshop_page/index1.html', {})

def petshop_about(request):
    return render(request, 'petshop_page/about.html', {})

def petshop_blog(request):
    return render(request, 'petshop_page/blog.html', {})

def petshop_contact(request):
    return render(request, 'petshop_page/contact.html', {})

def petshop_detail(request):
    return render(request, 'petshop_page/detail.html', {})

def purr_about(request):
    return render(request, 'purr_page/about.html', {})

def purr_contact(request):
    return render(request, 'purr_page/contact.html', {})

def purr_gallery(request):
    return render(request, 'purr_page/gallery.html', {})

def purr_index(request):
    return render(request, 'purr_page/index.html', {})
