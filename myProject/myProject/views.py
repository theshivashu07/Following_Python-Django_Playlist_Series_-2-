
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm
from service.models import Service,trialData
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import saveEnquiry

# we importing this, because of email sending purpose...
from django.core.mail import send_mail



def index(request):
    newsData=News.objects.all()[1:];
    data={
        'newsData' : newsData,
    }
    return render(request,'index.html',data);

def newsdetails(request,newsslug):
    newsDetails=News.objects.get(slug=newsslug);
    data={
        'newsdetails' : newsDetails,
    }
    return render(request,'newsdetails.html',data); 

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
            if request.POST["firstvalue"]=="":
                data={'error':True}
                return render(request,'EVENODD.html',data); 
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





def marksheet(request):
    data={}
    try:
        if request.method=="POST":
            # use eval, if int or float then okay, otherwise give error.
            mark1=eval(request.POST["firstmark"]);
            mark2=eval(request.POST["secondmark"]);
            mark3=eval(request.POST["thirdmark"]);
            mark4=eval(request.POST["fourthmark"]);
            mark5=eval(request.POST["fifthmark"]);
            total = mark1+mark2+mark3+mark4+mark5
            persentage=(total*100)/500;
            division= "First" if(persentage>=60) else ["Second" if(persentage>=48) else [ "Third" if(persentage>=33) else "Fail"]]
            division= division if(division=="Fail") else division+" Division";
            data={
                'firstmark' : mark1, 
                'secondmark' : mark2, 
                'thirdmark' : mark3, 
                'fourthmark' : mark4, 
                'fifthmark' : mark5, 
                'total' : total, 
                'persentage' : persentage, 
                'division' : division, 
            }
    except:
        data={
            'firstmark' : mark1, 
            'secondmark' : mark2, 
            'thirdmark' : mark3, 
            'fourthmark' : mark4, 
            'fifthmark' : mark5, 
            'result':"Something WRONG : Enter Correct Inputs!", 
        } 
    print(data); 
    return render(request,'MARKSHEET.html',data);




def getalltabledata(request):
    gettingData=trialData.objects.all();
    if request.method=="GET":
        value=request.GET.get('servicename');
        if value!=None:
            # gettingData=trialData.objects.filter(head_data=value);
            # select *from tablename where tablename title='head_data'
            # ------------------------------------
            gettingData=trialData.objects.filter(head_data__icontains=value);
            # // with it we search word in both side, below syntax is not as it is!
            # select *from service where service title likes '% worddata %'
    data={
        'gettingData':gettingData,
    }
    return render(request,'GetAllTableData.html',data);




def pagination(request):
    gettingData=trialData.objects.all();
    paginator=Paginator(gettingData,2)
    pageNo=request.GET.get('page');
    gettingDataFinal=paginator.get_page(pageNo)
    lastpageNo=gettingDataFinal.paginator.num_pages
    data={
        'gettingData':gettingDataFinal,
        'lastpageNo':lastpageNo,
        'mylist':[ i+1 for i in range(lastpageNo)],
    }
    return render(request,'PAGINATION.html',data);






def saveenquiry(request):
    data={}
    if request.method=="POST":
        my_name=request.POST["myname"]
        my_email=request.POST["myemail"]
        my_mno=request.POST["mymno"]
        my_websitename=request.POST["mywebsitename"]
        my_message=request.POST["mymessage"]
        values=saveEnquiry(my_name=my_name, my_email=my_email, my_mno=my_mno, my_websitename=my_websitename, my_message=my_message);
        values.save()
        data={
            'myname' : my_name,
            'myemail' : my_email,
            'mymno' : my_mno,
            'mywebsitename' : my_websitename,
            'mymessage' : my_message,
            'message' : "<center><b style='color: red;'>Your Data Is Inserted Successfully!</b></center>"
        }
    return render(request,'TestingForm.html',data);


def showuserinformations(request):
    gettingData=saveEnquiry.objects.all();
    data={
        'gettingData':gettingData,
    }
    return render(request,'ShowUserInformations.html',data);





def sentmail(request):   
    send_mail(
        'Testing-Mail',
        'This mail is sent by just only the testing purpose.',
        'djangotrial07@gmail.com',
        ['shivamshukla3108@gmail.com'],
        fail_silently=False,
    )
    return render(request,'index.html');








