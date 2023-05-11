from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from home.models import studData
from home.models import teacherData
from home.models import questions
from home.models import test,trial,result
from django.contrib import messages 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from hello import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from .models import result
from django.views.generic import TemplateView
from django.db.models import Avg

 
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
@login_required(login_url='loginstudent')
def student(request):
    # login(request)
    # fname = user.first_name
    # fname=fname
    return render(request, 'student/student.html')

@login_required(login_url='loginstudent')
def student2(request):
    # fname=fname
    return render(request, 'student/student2.html')

@login_required(login_url='loginstudent')
def quiz(request):
    # login(request)
    data = test.objects.filter(datee=datetime.now().date(),subject="DSA")
    data1 = test.objects.filter(datee=datetime.now().date(),subject="SE")
    data2 = test.objects.filter(datee=datetime.now().date(),subject="JP")
    # sub = test.objects.get('subject') 
    # if sub == "DSA":
    #     return render(request, 'my_template.html', {'sub': sub})
    # if sub == "JAVA":
    #     return render(request, 'my_template.html', {'sub': sub})
    # if sub == "SE":
    #     return render(request, 'my_template.html', {'sub': sub})
    return render(request, 'student/quiz.html',{'data':data,'data1':data1,'data2':data2})

@login_required(login_url='loginstudent')
def schedule(request):
    # login(request)
    data = test.objects.all()
    print(data)
    return render(request, 'student/schedule.html',{'data':data})
    
def loginstudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # user.is_active=True
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
    # user.is_active=False
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
    login(request)
    data = test.objects.all()
    return render(request, 'teacher/teacher.html',{'data':data})

def trial(request):
    return render(request, 'teacher/trial.html')

def loginteacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            # user.is_active()
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


@login_required(login_url='loginteacher')
def addQuestion(request):
    if request.method == "POST":
        subject=request.POST.get('subject')
        topic=request.POST.get('topic')
        question=request.POST.get('question')
        op1=request.POST.get('op1')
        op2=request.POST.get('op2')
        op3=request.POST.get('op3')
        op4=request.POST.get('op4')
        correct=request.POST.get('correct')
        diff=request.POST.get('diff')
        
        addQuestion=questions(subject=subject,topic=topic,question=question,op1=op1,op2=op2,op3=op3,op4=op4,correct=correct,diff=diff)
        addQuestion.save()
        messages.success(request,'Question added to Database')
        return redirect('/addQuestion')
    # return render()
    return render(request, 'teacher/teacher.html')

@login_required(login_url='loginteacher')
def setTest(request):
    # login()
    if request.method == "POST":
        subject=request.POST.get('subject')
        qno=request.POST.get('qno')
        datee=request.POST.get('datee')
        
        setTest=test(subject=subject,qno=qno,datee=datee)
        setTest.save()
        messages.success(request,'Test created successfully')
        
        # EMAIL
        users = studData.objects.all()
        for user in users:
            subject = 'New Test set'
            message = 'Hi ' + user.fname + ', \nA test on '+ setTest.subject +' has been created for '+setTest.datee+'.\n ALL THE BEST!!!!!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        return redirect('/setTest')
    return render(request, 'teacher/teacher.html')

@login_required(login_url='loginstudent')
def DSA(request):
    if request.method == 'POST':
        print(request.POST)
        question1=questions.objects.filter(subject='DSA').order_by('?')[:10]
        score=0
        wrong=0
        correct=0
        total=0
        for q in question1:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct)
            print()
            if q.correct ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        
        
        res=result(score=score,datee=datetime.today(),subject="DSA")
        
        res.save()
        
        average_score = result.objects.filter(subject='DSA').aggregate(Avg('score'))['score__avg']
        average_score = round(average_score, 2)
        average_score=average_score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'average':average_score,
        }
        return render(request,'student/result.html',context)
    else:
        question1=questions.objects.filter(subject='DSA').order_by('?')[:10]
        context = {
            'question1':question1
        }
        return render(request,'student/DSA.html',context)
    
def score_view(request):
    score = request.GET.get('score')
    
    context = {'score': score}
    return render(request, 'score.html', context)


@login_required(login_url='loginstudent')
def JAVA(request):
    if request.method == 'POST':
        print(request.POST)
        question1=questions.objects.filter(subject='JP').order_by('?')[:10]
        score=0
        wrong=0
        correct=0
        total=0
        for q in question1:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct)
            print()
            if q.correct ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        
        res=result(score=score,datee=datetime.today(),subject="JP")
        
        res.save()
        
        average_score = result.objects.filter(subject='JP').aggregate(Avg('score'))['score__avg']
        average_score = round(average_score, 2)
        average_score=average_score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'average':average_score,
        }
        return render(request,'student/result.html',context)
    else:
        question1=questions.objects.filter(subject='JP').order_by('?')[:10]
        context = {
            'question1':question1
        }
        return render(request,'student/JAVA.html',context)

@login_required(login_url='loginstudent')
def SE(request):
    if request.method == 'POST':
        print(request.POST)
        question1=questions.objects.filter(subject='SE').order_by('?')[:10]
        score=0
        wrong=0
        correct=0
        total=0
        for q in question1:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct)
            print()
            if q.correct ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        res=result(score=score,datee=datetime.today(),subject="SE")
        
        res.save()
        
        average_score = result.objects.filter(subject='SE').aggregate(Avg('score'))['score__avg']
        average_score = round(average_score, 2)
        average_score=average_score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'average':average_score,
        }
        return render(request,'student/result.html',context)
    else:
        question1=questions.objects.filter(subject='SE').order_by('?')[:10]
        context = {
            'question1':question1
        }
        return render(request,'student/SE.html',context)

def example1(request):
    exam = trial.objects.all()
    return render(request,"example1.html",{"exam":exam})


def try1(request):
    if request.method == 'POST':
        print(request.POST)
        question1=questions.objects.filter(subject='SE').order_by('?')[:10]
        score=0
        wrong=0
        correct=0
        total=0
        for q in question1:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct)
            print()
            if q.correct ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'student/result.html',context)
    else:
        question1=questions.objects.filter(subject='SE').order_by('?')[:10]
        context = {
            'question1':question1
        }
        return render(request,'student/try1.html',context)
    
# def quiz_chart(request):
#     # Get the data for the chart
#     quiz_results = result.objects.all()
#     labels = []
#     scores = []
    
#     for quiz_result in quiz_results:
#         labels.append(quiz_result.datee.strftime("%Y-%m-%d"))
#         scores.append(quiz_result.score)
        
#     return render(request,'charts.html',{
#         "labels":labels,
#         "scores":scores,
#     })
#     # Return the data as a JSON response
#     # data = {
#     #     "labels": labels,
#     #     "data": scores
#     # }
#     # return JsonResponse(data)

# class chart(TemplateView):
#     template_name="charts.html"
    
#     def get_context_data(self, **kwargs) :
#         context=super().get_context_data(**kwargs)
#         context["qs"] = result.objects.all()
        
        # return context
        
        



    