from django.shortcuts import render,redirect
from .models import Supplier
from .forms import SupplierCreateForm,SupplierUpdateForm

# Create your views here.
def list_supplier(request):
    queryset = Supplier.objects.all()
    form = SupplierCreateForm(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'supplier/index.html',context)
def create_supplier(request):
    form =  SupplierCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/supplier/list_category/')
    context = {
        "form":form,
    }    
    return render(request,'supplier/create.html',context)
def update_supplier(request,pk):
    queryset = Supplier.objects.get(id=pk)
    form = SupplierUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = SupplierUpdateForm(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/supplier/list_category/')
    context = {
            "form":form,
        }
    return render(request,'supplier/update.html',context)

def delete_supplier(request,pk):
    queryset = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/supplier/list_category/')
    return render(request,'supplier/delete.html')
