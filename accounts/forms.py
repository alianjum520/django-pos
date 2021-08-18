from django import forms
from .models import Account_Type,Account_Category,Account_Area,Account

class create_account_type(forms.ModelForm):
    class Meta:
        model = Account_Type
        fields = ['name','account_type']
class create_account_category(forms.ModelForm):
    class Meta:
        model = Account_Category
        fields = ['category_name']
class create_account_area(forms.ModelForm):
    class Meta:
        model = Account_Area
        fields = ['area_name']
class create_account(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','phone','landline','Bank_id','Bank_Name','opening_credit','opening_debit','ntn','cnic','Address','current_cr','current_dr','licensce_number','expairy_date','security_check']
class update_account_type(forms.ModelForm):
    class Meta:
        model = Account_Type
        fields = ['name','account_type']
class update_account_category(forms.ModelForm):
    class Meta:
        model = Account_Category
        fields = ['category_name']
class update_account_area(forms.ModelForm):
    class Meta:
        model = Account_Area
        fields = ['area_name']
class update_account(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','type','category','area','phone','landline','Bank_id','Bank_Name','opening_credit','opening_debit','ntn','cnic','Address','current_cr','current_dr','licensce_number','expairy_date','security_check']
class account_create_form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name','type','category','area','phone','landline','Bank_id','Bank_Name','opening_credit','opening_debit','ntn','cnic','Address','current_cr','current_dr','licensce_number','expairy_date','security_check']