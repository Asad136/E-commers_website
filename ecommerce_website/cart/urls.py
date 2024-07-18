from django.urls import path
from . import views
app_name='cart'

urlpatterns = [
    path('',views.cart_summery,name='cart_summery'),
    # path('add/',views.cart_add,name='cart_add'),
    # path('update/',views.update,name='cart_update'),
    # path('delete/',views.cart_delete,name='cart_delete'),

]
