

from django.urls import path
from employee import views

app_name = 'employee'
urlpatterns = [
    path('output/', views.employee_output, name = 'employee_list'),
    path('input/', views.employee_input, name = 'employee_input'),
]
