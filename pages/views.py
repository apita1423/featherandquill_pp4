from django.shortcuts import render
from django.views import generic, View

def home(request):
    return render(request, 'pages/home.html')