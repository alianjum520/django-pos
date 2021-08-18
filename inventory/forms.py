from django import forms
from .models import Product,Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['refno','name','category','cost_price','selling_price','quantity','description']

class StockSearch(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['refno','name','category','cost_price','selling_price','quantity','description']