
from django.http import HttpResponse 


def aboutus(request):
        return HttpResponse("<b>Welcome to shivashu.com</b>")
def course(request):
        return HttpResponse("Welcome to Python")
def courseDetails(request,courseid):
    return HttpResponse(courseid)


























