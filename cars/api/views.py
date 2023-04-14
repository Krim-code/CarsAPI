from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello!</h1>')