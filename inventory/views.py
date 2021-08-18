from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import StockCreateForm,StockSearch,StockUpdateForm, CategoryCreateForm,CategoryUpdateForm

# Create your views here.
def list_products(request):
    queryset = Product.objects.all()
    form = StockSearch(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    if request.method == 'POST':
        queryset = Product.objects.filter(refno__icontains=form['refno'].value(),
                                        name__icontains=form['name'].value(),
                                        category__icontains=form['category'].value() )
        context = {
            "form":form,
            'queryset':queryset
        }
    return render(request,'store/product_list.html',context)
def list_category(request):
    queryset = Category.objects.all()
    form = CategoryCreateForm(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'store/category_list.html',context)
def create_category(request):
    form =  CategoryCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/inventory/list_category/')
    context = {
        "form":form,
    }    
    return render(request,'store/create_category.html',context)
def update_category(request,pk):
    queryset = Category.objects.get(id=pk)
    form = CategoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/inventory/list_category/')
    context = {
            "form":form,
        }
    return render(request,'store/update_category.html',context)

def delete_category(request,pk):
    queryset = Category.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/inventory/list_category/')
    return render(request,'store/delete_category.html')

def create_product(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/inventory/list/')
    context = {
        "form":form,
    
    }    
    return render(request,'store/create_product.html',context)
def update_products(request,pk):
    queryset = Product.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/inventory/list/')
    context = {
            "form":form,
        }
    return render(request,'store/update_product.html',context)

def delete_products(request,pk):
    queryset = Product.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/inventory/list/')
    return render(request,'store/delete_product.html')