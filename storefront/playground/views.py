from django.shortcuts import render
from django.http import HttpResponse

def say_hello(resuest):
    return HttpResponse('Hello world')
