from django.contrib import admin
from home.models import Contact
from home.models import studData
from home.models import teacherData

 # Register your models here.
admin.site.register(Contact)
admin.site.register(studData)
admin.site.register(teacherData)