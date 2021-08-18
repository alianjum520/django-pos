from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    refno = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=400,blank=True,null=True)
    

    def __str__(self):
        return self.name
