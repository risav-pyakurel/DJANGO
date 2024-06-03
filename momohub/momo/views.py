from django.shortcuts import render

# Create your views here.

def all_momo(request):
    return render(request, 'momo/all_momo.html')