from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse

def cart_summery(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, "cart/cart_summery.html", {"cart_products": cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1)) 
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'cart_quantity': cart_quantity})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.update(product=product, quantity=quantity)
        response = JsonResponse({'success': True})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        response = JsonResponse({'success': True})
        return response
