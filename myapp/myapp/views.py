from django.http import HttpResponse
import datetime

def test(request):
  date= datetime.datetime.now()
  print("test function is called from view")
  return HttpResponse(" <h1> Hello this is index page  </h1> " +str(date))

def about(request):
  return HttpResponse(" <h1> <i>This is about page</i></h1>")

def services(request):
  return HttpResponse(" <h1> <i>This is our Service page</i></h1>")
