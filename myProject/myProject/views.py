
from django.http import HttpResponse, HttpResponseRedirect
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
    # data={}  # its must because if not passes values to data variable is like error, because its not showing anywhere and directly we use it.
    try:
        if request.method=="POST":
            # Both ways working correctly!
            val1=int(request.POST["firstvalue"]);
            val2=int(request.POST["secondvalue"]);
            # val1=int(request.POST.get("firstvalue"));
            # val2=int(request.POST.get("secondvalue"));
            print(val1+val2); 
            '''
            data={
                'firstvalue' : val1,
                'secondvalue' : val2,
                'addition' : val1+val2,
                'multiplication' : val1*val2,
            }
            '''
            url='/userformresult/?addition={0}&multiplication={1}'.format(val1+val2,val1*val2)
            # return HttpResponseRedirect(url);     # first way
            return redirect(url);     # second way
    except:
        pass
    return render(request,'USERFORM.html');

def userformresult(request):
    data={}
    if request.method=="GET":
        addition=request.GET.get('addition');
        multiplication=request.GET.get('multiplication');
        data={'addition':addition, 'multiplication':multiplication}
    return render(request,'USERFORMRESULT.html',data);






















