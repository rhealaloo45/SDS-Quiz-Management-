from django.contrib import admin
from django.urls import path
from home import views
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('entrys',views.entrys, name='entrys'),
    # path('student',views.student, name='student'),
    path('loginstudent',views.loginstudent, name='loginstudent'),
    path('signupstudent',views.signupstudent, name='signupstudent'),
    path('signoutstudent',views.signoutstudent, name='signoutstudent'),
    # path('entryt',views.entryt, name='entryt'),
    path('loginteacher',views.loginteacher, name='loginteacher'),
    # path('signupteacher',views.signupteacher, name='signupteacher'),
    # path('signoutteacher',views.signoutteacher, name='signoutteacher'),
]