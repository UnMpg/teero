from django.shortcuts import render

# Create your views here.
def controlpage(request): 
    return render(request, 'controls/control.html')