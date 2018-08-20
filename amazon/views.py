from django.shortcuts import render
from amazon.forms import IssueInput
from amazon.models import IssueTracking

# Create your views here.

def amazon_output(request):
    amazon_output = IssueTracking.objects.order_by('po')
    return render(request, 'amazon/amazon_output.html', {'amazon_output': amazon_output})

def amazon_input(request):
    amazon_in = IssueInput()
    if request.method =='POST':
        amazon_in = IssueInput(request.POST)
        if amazon_in.is_valid():
            amazon_in.save(commit = True)
            return amazon_output(request)
        else:
            print('Error in input')
    return render(request, 'amazon/amazon_input.html', {'amazon_in': amazon_in})
