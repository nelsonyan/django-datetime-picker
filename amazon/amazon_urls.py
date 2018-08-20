

from django.urls import path
from amazon import views

app_name = 'amazon'
urlpatterns = [
    path('input/', views.amazon_input, name = 'input'),
    path('output/', views.amazon_output, name = 'output'),
]
