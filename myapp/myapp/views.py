from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
  date= datetime.datetime.now()
  print("test function is called from view")
  #return HttpResponse(" <h1> Hello this is index page  </h1> " +str(date))
  return render(request,"home.html",{})

def about(request):
  #return HttpResponse(" <h1> <i>This is about page</i></h1>")
  return render(request, "about.html", {})


def services(request):
  #return HttpResponse(" <h1> <i>This is our Service page</i></h1>")
  return render(request, "services.html", {})
