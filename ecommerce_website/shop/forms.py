from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category,Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','description','price','stock']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=70,help_text='Required. enter a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')