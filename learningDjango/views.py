from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is home page.")
    return render(request, 'website/home.html')

def about(request):
    # return HttpResponse("This is about page.")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("This is contact page.")
    return render(request, 'website/contact.html')