from django.shortcuts import render

def cart_summery(request):
    return render(request, "cart/cart_summery.html")
