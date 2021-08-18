from django import forms
from .models import Supplier


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone_no','product','company','description']
class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone_no','product','company','description']

