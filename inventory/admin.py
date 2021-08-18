from django.contrib import admin
from .models import Product,Category
from .forms import StockCreateForm

class StockAdminCreate(admin.ModelAdmin):
    list_display = ['refno','name','category','cost_price','selling_price','quantity','description']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['refno','name','category']


admin.site.register(Product, StockAdminCreate)
admin.site.register(Category)