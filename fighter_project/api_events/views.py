from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is our homepage")

def profile(request):
    return render(request, 'profile.html', {})

def events(requests):
    return HttpResponse("This is our events page bruh")