from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):

    return HttpResponse("hello")


def base(request):

    return HttpResponse("this is base function")