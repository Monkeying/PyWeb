from django.http import HttpResponse
from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.

def Login(request):
    return render(request, 'Login.html')
    # return HttpResponse("Hello world ! ")

def authentic(request):
    return HttpResponse("Hello world ! ")

def user(request):
    return HttpResponse("Hello world ! ")

def devices(request):
    return HttpResponse("Hello world ! ")

def device(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'devices.html' )


