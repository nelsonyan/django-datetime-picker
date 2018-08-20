from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home.html', {'welcome_message': 'Welcome home'})
