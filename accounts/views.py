from django.shortcuts import render,redirect
from.models import Account_Type,Account_Category,Account_Area,Account
from .forms import create_account_type,create_account_category,create_account_area,create_account,update_account,update_account_area,update_account_category,update_account_type
# Create your views here.
def list_type(request):
    queryset = Account_Type.objects.all()
    form = create_account_type(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'accounts/account_type/index.html',context)

def create_type(request):
    form =  create_account_type(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form":form,
    }    
    return render(request,'accounts/account_type/create_account_type.html',context)
def list_category(request):
    queryset = Account_Category.objects.all()
    form = create_account(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'accounts/accountcategory/index.html',context)
def create_category(request):
    form =  create_account_category(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form":form,
    }    
    return render(request,'accounts/accountcategory/create_account_caategory.html',context)
def list_area(request):
    queryset = Account_Area.objects.all()
    form = create_account(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'accounts/accountarea/index.html',context)

def create_area(request):
    form =  create_account_area(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form":form,
    }    
    return render(request,'accounts/accountarea/create_account_area.html',context)
def list_account(request):
    queryset = Account.objects.all()
    form = create_account(request.POST or None)
    context = {
        'queryset':queryset,
        "form":form
    }
    return render(request,'accounts/account/index.html',context)
def create(request):
    form =  create_account(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form":form,
    }    
    return render(request,'accounts/account/create_account.html',context)
def update_type(request,pk):
    queryset =  Account_Type.objects.get(id=pk)
    form = update_account_type(instance=queryset)
    if request.method == 'POST':
        form = update_account_type(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/accounts/list_type/')
    context = {
            "form":form,
        }
    return render(request,'accounts/account_type/update_account_type.html',context)
def update_category(request,pk):
    queryset = Account_Category.objects.get(id=pk)
    form = update_account_category(instance=queryset)
    if request.method == 'POST':
        form = update_account_category(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/accounts/list_category/')
    context = {
            "form":form,
        }
    return render(request,'accounts/accountcategory/update_account_category.html',context)
def update_area(request,pk):
    queryset = Account_Area.objects.get(id=pk)
    form = update_account_area(instance=queryset)
    if request.method == 'POST':
        form = update_account_area(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/accounts/list_area/')
    context = {
            "form":form,
        }
    return render(request,'accounts/accountarea/update_account_area.html',context)
def update(request,pk):
    queryset = Account.objects.get(id=pk)
    form = update_account(instance=queryset)
    if request.method == 'POST':
        form = update_account(request.POST,instance=queryset) 
        if form.is_valid():
            form.save()
            return redirect('/accounts/list_account/')
    context = {
            "form":form,
        }
    return render(request,'accounts/account/update_account.html',context)
def delete_type(request,pk):
    queryset = Account_Type.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/accounts/list_type/')
    return render(request,'accounts/account_type/delete.html')
def delete_category(request,pk):
    queryset = Account_Category.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/accounts/list_category/')
    return render(request,'accounts/accountcategory/delete.html')
def delete_area(request,pk):
    queryset = Account_Area.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/accounts/list_area/')
    return render(request,'accounts/accountarea/delete.html')
def delete(request,pk):
    queryset = Account.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/accounts/list_account/')
    return render(request,'accounts/account/delete.html')