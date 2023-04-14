from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request, *args, **kwargs):
    template = loader.get_template('index.html')
    return render(request, 'index.html')


