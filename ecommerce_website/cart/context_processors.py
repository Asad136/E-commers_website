from .cart import Cart
# this will make it available in whole app
def cart(request):
    return { 'cart':Cart(request)}