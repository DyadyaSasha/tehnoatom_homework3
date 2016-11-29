from django.shortcuts import render

# Create your views here.

def base_page(request):
    return render(request, 'main.html')

def charges(request):
    return render(request, 'table.html')    