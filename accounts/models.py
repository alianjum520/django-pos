from django.db import models

# Create your models here.
class Account_Type(models.Model):
    name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Account_Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
class Account_Area(models.Model):
    area_name = models.CharField(max_length=200)
    def __str__(self):
        return self.area_name
class Account(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Account_Type,on_delete=models.CASCADE)
    category = models.ForeignKey(Account_Category,on_delete=models.CASCADE)
    area =  models.ForeignKey(Account_Area,on_delete=models.CASCADE)
    phone = models.CharField(max_length=200,blank=True,null=True)
    landline = models.CharField(max_length=200,blank=True,null=True)
    Bank_id = models.CharField(max_length=200,blank=True,null=True)
    Bank_Name = models.CharField(max_length=200,blank=True,null=True)
    opening_credit = models.FloatField()
    opening_debit = models.FloatField()
    ntn = models.CharField(max_length=200,blank=True,null=True)
    cnic = models.CharField(max_length=200,blank=True,null=True)
    JoiningDate = models.DateField(auto_now_add=True)
    Address = models.CharField(max_length=200,blank=True,null=True)
    current_cr = models.FloatField()
    current_dr = models.FloatField()
    licensce_number = models.CharField(max_length=200,blank=True,null=True)
    expairy_date = models.DateField(blank=True,null=True)
    security_check = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.name