
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls',namespace='shop')),
    path('account/', include('account.urls', namespace='account')),
    path('cart/',include('cart.urls',namespace='cart')),

]
