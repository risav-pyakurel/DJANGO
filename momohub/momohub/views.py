from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1> Hello, OOMFIES. You are at momohub")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("<h1> Momohub is all about finding best momo place is Nepal")

def contact(request):
    return HttpResponse("<h1>Please contact us to get featured in our site")
