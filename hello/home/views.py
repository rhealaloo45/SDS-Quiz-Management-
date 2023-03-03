from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
 
def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'this is sent2'
    }
    # messages.success(request,"This is a test  message")
    return render(request, 'index.html',context)
    # return HttpResponse("This is  homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is  aboutpage")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is  servicespage")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')



    # return HttpResponse("This is  contactpage")
# Create your views here.
