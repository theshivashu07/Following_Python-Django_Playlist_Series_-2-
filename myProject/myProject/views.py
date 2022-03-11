
from django.http import HttpResponse 
from django.shortcut import render


def homepage(request):
    return render(request,"index.html")
def aboutus(request):
        return HttpResponse("<b>Welcome to shivashu.com</b>")
def course(request):
        return HttpResponse("Welcome to Python")
def courseDetails(request,courseid):
    return HttpResponse(courseid)


























