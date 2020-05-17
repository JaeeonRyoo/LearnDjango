from django.shortcuts import render

from .models import Food

def index(request):
    return render(request, 'tasty/index.html', {})