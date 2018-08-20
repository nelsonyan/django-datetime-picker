

from django import forms
from employee.models import EmployeeList

class EmployeeInput(forms.ModelForm):
    class Meta():
        model = EmployeeList
        fields = '__all__'
