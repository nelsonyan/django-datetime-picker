from django.contrib import admin
from employee.models import Department, EmployeeList

# Register your models here.

admin.site.register(Department)
admin.site.register(EmployeeList)
