# Ex02 Django ORM Web Application

# AIM/
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2025-03-25 214231.png>)
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```

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


from django.contrib import admin

from .models import Bank,BankAdmin

admin.site.register(Bank,BankAdmin)
```
# OUTPUT
Include the screenshot of your admin page.
![alt text](<Screenshot 2025-03-25 211359.png>)
![alt text](<Screenshot 2025-03-25 212003.png>)
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
/
