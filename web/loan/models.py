
from django.db import models

from django.contrib import admin

class Bank(models.Model):

    date_of_birth=models.DateField(default=0)
    
    name=models.CharField(max_length=70,default=0)
    
    age=models.IntegerField(default=0)
    
    customerid=models.IntegerField(primary_key="customerid",default=0)
    
    accountdetails=models.CharField(max_length=70,default=0)

class BankAdmin(admin.ModelAdmin):
    
    list_display=('name','date_of_birth','age','customerid','accountdetails')

# Create your models here.
