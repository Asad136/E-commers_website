from django.urls import path
from . import views
app_name ='shop'

urlpatterns = [
    path('shop/', views.admin_dashboard, name='admin_dashboard'),
    path('shop/category/add/', views.add_category, name='add_category'),
    path('shop/category/update/<int:pk>/', views.update_category, name='update_category'),
    path('shop/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('shop/product/add/', views.add_product, name='add_product'),
    path('shop/product/update/<int:pk>/', views.update_product, name='update_product'),
    path('shop/product/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('', views.index, name='index'),
    path('shop/category/<int:pk>/', views.category_detail, name='category_detail'),
]
