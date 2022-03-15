
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm


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
    func=userForm()
    data={'form':func}
    try:
        if request.method=="POST":
            # Both ways working correctly!
            val1=int(request.POST["firstvalue"]);
            val2=int(request.POST["secondvalue"]);
            # val1=int(request.POST.get("firstvalue"));
            # val2=int(request.POST.get("secondvalue"));
            #print(val1+val2); 
            data={
                'form':func,
                'firstvalue' : val1,
                'secondvalue' : val2,
                'addition' : val1+val2,
                'multiplication' : val1*val2,
            }
            url='/userformresult/?addition={0}&multiplication={1}'.format(val1+val2,val1*val2)
            # return HttpResponseRedirect(url);     # first way
            return redirect(url);     # second way
    except:
        pass
    return render(request,'USERFORM.html',data);

def userformresult(request):
    data={}
    if request.method=="GET":
        addition=request.GET.get('addition');
        multiplication=request.GET.get('multiplication');
        data={'addition':addition, 'multiplication':multiplication}
    return render(request,'USERFORMRESULT.html',data);


def submitform(request):
    try:
        if request.method=="POST":
            val1=int(request.POST["firstvalue"]);
            val2=int(request.POST["secondvalue"]);
            url='/userformresult/?addition={0}&multiplication={1}'.format(val1+val2,val1*val2)
            print("By 'submitform' URL");
            # return HttpResponseRedirect(url);     # first way
            return redirect(url);     # second way
    except:
        pass
    return render(request,'USERFORM.html');


def calculator(request):
    data={}
    try:
        if request.method=="POST":
            val1=request.POST["firstvalue"];
            val2=request.POST["secondvalue"];
            optr=request.POST["opr"];

            """
            # If you write required field on label tag, so there is must to pass anything there, then no need to write here so long code.
            if(optr==""):
                data={
                    'firstvalue' : val1,
                    'secondvalue' : val2,
                    'result':"Something WRONG : Select Operator Also!"
                    # 'result':"<b style='color: red;'>Select Operator Also!</b>"
                }
            else:
                data={
                    'firstvalue' : val1,
                    'secondvalue' : val2,
                    'result' : eval(val1+optr+val2),
                }
                """
            # you only write that code!
            data={
                'firstvalue' : val1,
                'secondvalue' : val2,
                'result' : eval(val1+optr+val2),
            }
    except:
        data={
            'firstvalue' : val1,
            'secondvalue' : val2,
            'result':"Something WRONG : Enter Correct Inputs!"
        }
    return render(request,'CALCULATOR.html',data);


















