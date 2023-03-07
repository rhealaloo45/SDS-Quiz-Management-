from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from home.models import studData
from home.models import teacherData
from django.contrib import messages 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hello import settings
from django.contrib.auth import authenticate,login,logout

 
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

# def entrys(request):
#     return render(request, "student/entrys.html")

def student(request):
    return redirect('student')

def loginstudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "student/student.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'student/loginstudent.html')


def signupstudent(request):
    if request.method == "POST":
            # username = request.POST.get('username')
            username = request.POST['username']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('home')
        
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, "Email Already Registered!!")
            #     return redirect('entrys')
        
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('home')
        
            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('home')
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('home')
            
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            
            myuser.save()
            
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            # Welcome Email
            subject = "Welcome to Student diagnostics system!!"
            message = "Hello " + myuser.first_name + "!! \n" + "Welcome to SDS!! \nThank you for visiting our website.\nWe have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSDS"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            
            # USEER DATA SAVING
            username=request.POST.get('username')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            # pass1=request.POST.get('pass1')
            sid=request.POST.get('sid')
            phone=request.POST.get('phone')
            parphone=request.POST.get('parphone')
            branch=request.POST.get('branch')
            year=request.POST.get('year')
            # sem=request.POST.get('sem')
            signupstudent=studData(username=username,fname=fname,lname=lname,email=email,sid=sid,phone=phone,parphone=parphone,branch=branch,year=year,date=datetime.today())
            
            signupstudent.save()
            messages.success(request,'Registration Successfull')
            
            return redirect('/loginstudent')
    return render(request, 'student/signupstudent.html')

def signoutstudent(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

# def student(request):
#     return render(request, 'student/student.html')
    # return HttpResponse("This is  contactpage")
# Create your views here.


#TEACHER PART
# def entryt(request):
#     return render(request, "teacher/entryt.html")
def teacher(request):
    return redirect('teacher')

def loginteacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "teacher/teacher.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'teacher/loginteacher.html')

def signupteacher(request):
    if request.method == "POST":
            # username = request.POST.get('username')
            username = request.POST['username']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('home')
        
            # if User.objects.filter(email=email).exists():
            #     messages.error(request, "Email Already Registered!!")
            #     return redirect('entrys')
        
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('home')
        
            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('home')
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('home')
            
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            
            myuser.save()
            
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            # Welcome Email
            subject = "Welcome to Student diagnostics system!!"
            message = "Hello " + myuser.first_name + "!! \n" + "Welcome to SDS!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSDS"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            
            # USEER DATA SAVING
            username=request.POST.get('username')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            # pass1=request.POST.get('pass1')
            tid=request.POST.get('tid')
            phone=request.POST.get('phone')
            # officephone=request.POST.get('officephone')
            branch=request.POST.get('branch')
            year=request.POST.get('year')
            # sem=request.POST.get('sem')
            signupteacher=teacherData(username=username,fname=fname,lname=lname,email=email,tid=tid,phone=phone,branch=branch,year=year,date=datetime.today())
            
            signupteacher.save()
            messages.success(request,'Registration Successfull')
            
            return redirect('/loginteacher')
    return render(request, 'teacher/signupteacher.html')

def signoutteacher(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')