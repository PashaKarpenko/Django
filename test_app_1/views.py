from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def foo(request: HttpRequest):
    return HttpResponse('Hello world!')

def first(request: HttpRequest):
    return HttpResponse('Bingo')
