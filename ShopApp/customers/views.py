from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is Customer App in ShopApp Django Website')