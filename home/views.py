from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def render_home(request: HttpRequest):
    return render(request, 'home/home.html')