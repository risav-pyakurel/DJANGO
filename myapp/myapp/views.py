from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
  if request.method == 'POST':
   check=request.POST['check']
   print(check)

  date= datetime.datetime.now()
  isActive =True
  name = "Momo and Code"
  list_of_programs= [
    'WAP to check the prime or composite',
    'WAP to check the odd or even',
    'WAP to print pascal triangles',
    'WAP to print all prime numbers from 1 to 100'
  ]

  student={
    'student_name' : "Risav",
    'student_college': "Amrit Science Campus ",
    'student_city': "Kathmandu"
  }
  #print("test function is called from view")
  #return HttpResponse(" <h1> Hello this is index page  </h1> " +str(date))
  data= {
    'date':date,
    'isActive':isActive,
    'name': name,
    'list_of_programs': list_of_programs,
    'student_data' : student

  }
  return render(request,"home.html",data)

def about(request):
  #return HttpResponse(" <h1> <i>This is about page</i></h1>")
  return render(request, "about.html", {})


def services(request):
  #return HttpResponse(" <h1> <i>This is our Service page</i></h1>")
  return render(request, "services.html", {})
