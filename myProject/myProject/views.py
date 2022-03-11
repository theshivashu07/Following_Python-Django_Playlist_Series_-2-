
from django.http import HttpResponse  
from django.shortcuts import render


def homepage(request):
    data={
        'title' : 'Home Page',
        'message' : 'Welcome to shivashu.com!',
        'mylist' : ['shivam','vashu','shivashu','shrivashu'],
    }
    return render(request,'index.html',data);

def aboutus(request):
    return HttpResponse("<b>Welcome to shivashu.com</b>");
def course(request):
    return HttpResponse("Welcome to Python");
def courseDetails(request,courseid):
    return HttpResponse(courseid)


























