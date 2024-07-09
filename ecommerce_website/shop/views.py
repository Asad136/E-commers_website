from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from django.contrib import messages
from .forms import CategoryForm, ProductForm,SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'shop/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def admin_required(user):
    return user.is_superuser

@user_passes_test(admin_required)
def admin_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/admin_dashboard.html', {'categories': categories, 'products': products})

@user_passes_test(admin_required)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = CategoryForm()
    return render(request, 'shop/add_category.html', {'form': form})

@user_passes_test(admin_required)
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/update_category.html', {'form': form})

@user_passes_test(admin_required)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_dashboard')
    return render(request, 'shop/delete_category.html', {'category': category})

@user_passes_test(admin_required)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

@user_passes_test(admin_required)
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/update_product.html', {'form': form})

@user_passes_test(admin_required)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    return render(request, 'shop/delete_product.html', {'product': product})

def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})
