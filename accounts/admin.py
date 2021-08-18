from django.contrib import admin
from .models import Account_Type,Account_Category,Account_Area,Account
from .forms import account_create_form
# Register your models here.
class account_admin_create(admin.ModelAdmin):
    list_display =['name','phone','landline','Bank_id','Bank_Name','opening_credit','opening_debit','ntn','cnic','Address','current_cr','current_dr','licensce_number','expairy_date','security_check']
    form = account_create_form
    list_filter = ['name']
    search_fields = ['name','phone']
admin.site.register(Account_Type)
admin.site.register(Account_Category)
admin.site.register(Account_Area)
admin.site.register(Account)