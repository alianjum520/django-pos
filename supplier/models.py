from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=11)
    product = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name