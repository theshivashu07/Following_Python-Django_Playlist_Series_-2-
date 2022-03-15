
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
            #...............................................
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




def evenodd(request):
    data={}
    try:   
        if request.method=="POST": 
            # use eval, if int or float then okay, otherwise give error. 
            value=eval(request.POST["firstvalue"]); 
            result = "Number is Even" if(value%2==0) else "Number is Odd"; 
            data={ 
                'firstvalue' : value, 
                'result' : result, 
            } 
    except: 
        data={ 
            'firstvalue' : value, 
            'result':"Something WRONG : Enter Correct Inputs!" 
        } 
    return render(request,'EVENODD.html',data); 





def prime(request):
    data={}
    try:
        if request.method=="POST":
            # use eval, if int or float then okay, otherwise give error.
            value=eval(request.POST["firstvalue"]);
            i=2
            while(i*i<=value):
                if(value%i==0):
                    result="Not Prime"
                    break
                i+=1;
            else:
                result="Prime";
            data={
                'firstvalue' : value,
                'result' : result,
            }
    except:
        data={
            'firstvalue' : value,
            'result':"Something WRONG : Enter Correct Inputs!"
        }
    return render(request,'PRIME.html',data);










