"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myProject import views

# these importing is must if we working with media related thing
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.index,name=""),
    path('index/',views.index, name="index"),
    path('newsdetails/<newsslug>',views.newsdetails, name="newsdetails"), 
    
    path('about-us/',views.aboutus, name="about-us"),
    path('services/',views.services, name="services"),
    # .......................................
    path('gallery/',views.gallery, name="gallery"),
    path('contact/',views.contact, name="contact"),
    path('userform/',views.userform, name="userform"), 
    path('userformresult/',views.userformresult, name="userformresult"), 
    
    path('submitform/',views.submitform, name="submitform"), 
    
    path('calculator/',views.calculator, name="calculator"), 
    path('evenodd/',views.evenodd, name="evenodd"), 
    path('prime/',views.prime, name="prime"), 
    path('marksheet/',views.marksheet, name="marksheet"), 

    path('getalltabledata/',views.getalltabledata, name="getalltabledata"), 
    path('pagination/',views.pagination, name="pagination"), 

    path('saveenquiry/',views.saveenquiry, name="saveenquiry"), 

    path('showuserinformations/',views.showuserinformations, name="showuserinformations"), 
    
    path('sentmail/',views.sentmail, name="sentmail"), 
    
    path('admin/', admin.site.urls),
]



# this is also must if we working with media related things
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



