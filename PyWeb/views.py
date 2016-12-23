from django.http import HttpResponse
from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.


def getlist(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'devices.html', context)

def hello(request):
	return HttpResponse("Hello world ! ")
