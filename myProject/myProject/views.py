
from django.http import HttpResponse  
from django.shortcuts import render



def index(request):
    return render(request,'index.html');

def aboutus(request):
    return render(request,'about-us.html');

def services(request):
    return render(request,'services.html');


# ...........................................


def gallery(request):
    return render(request,'gallery.html');

def contact(request):
    return render(request,'contact.html');
























