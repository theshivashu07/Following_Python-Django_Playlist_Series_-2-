
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

def userform(request):
    data={}  # its must because if not passes values to data variable is like error, because its not showing anywhere and directly we use it.
    try:
        # Both ways working correctly!
        val1=int(request.GET["firstvalue"]);
        val2=int(request.GET["secondvalue"]);
        # val1=int(request.GET.get("firstvalue"));
        # val2=int(request.GET.get("secondvalue"));
        # print(val1+val2); 
        data={
            'firstvalue' : val1,
            'secondvalue' : val2,
            'addition' : val1+val2,
            'multiplication' : val1*val2,
        }
    except:
        pass
    return render(request,'USERFORM.html',data);























