from django.shortcuts import render
from employee.models import EmployeeList
from employee.forms import EmployeeInput

# Create your views here.

def employee_output(request):
    employee_list = EmployeeList.objects.order_by('first_name')
    return render(request, 'employee/employee_temp.html', {'employee_list':employee_list})

def employee_input(request):
    employee_in = EmployeeInput()
    if request.method == 'POST':
        employee_in = EmployeeInput(request.POST)
        if employee_in.is_valid():
            employee_in.save(commit = True)
            return employee_output(request)
        else:
            print('Error in input')
    return render(request, 'employee/employee_input.html', {'employee_in': employee_in})
