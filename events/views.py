from django.shortcuts import render

# Create your views here.

def details(request):
    return render(request, 'events/details.html')

def list(request):
    return render(request, 'events/list.html')