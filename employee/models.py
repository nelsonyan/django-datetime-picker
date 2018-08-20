

from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.department


class EmployeeList(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True, blank = True)
    email = models.EmailField(unique = True)
    phone_ex = models.CharField(max_length = 10)
    cell = models.CharField(max_length = 20, blank = True)
    message = models.TextField(max_length = 2000, blank = True)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
