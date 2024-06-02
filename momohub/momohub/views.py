from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, OOMFIES. You are at momohub")


def about(request):
    return HttpResponse("<h1> Momohub is all about finding best momo place is Nepal")

def contact(request):
    return HttpResponse("Please contact us to get featured in our site")
