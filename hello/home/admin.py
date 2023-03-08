from django.contrib import admin
from home.models import Contact
from home.models import studData
from home.models import teacherData
from home.models import questions
from home.models import test

 # Register your models here.
admin.site.register(Contact)
admin.site.register(studData)
admin.site.register(teacherData)
admin.site.register(questions)
admin.site.register(test)