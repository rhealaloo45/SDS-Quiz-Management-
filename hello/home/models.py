from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=128)
    email= models.CharField(max_length=128) 
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
class studData(models.Model):
    username=models.CharField(max_length=100)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email= models.CharField(max_length=128) 
    sid=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    parphone=models.CharField(max_length=10)
    branch=models.CharField(max_length=40)
    year=models.CharField(max_length=8)
    # sem=models.CharField(max_length=4)
    date=models.DateField()
    
    def __str__(self):
        return self.fname
    
class teachData(models.Model):
    username=models.CharField(max_length=100)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email= models.CharField(max_length=128) 
    tid=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    # officephone=models.CharField(max_length=10)
    branch=models.CharField(max_length=40)
    year=models.CharField(max_length=8)
    # sem=models.CharField(max_length=4)
    date=models.DateField()
    
    def __str__(self):
        return self.fname
    
class teacherData(models.Model):
    username=models.CharField(max_length=100)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email= models.CharField(max_length=128) 
    tid=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    # officephone=models.CharField(max_length=10)
    branch=models.CharField(max_length=40)
    year=models.CharField(max_length=8)
    # sem=models.CharField(max_length=4)
    date=models.DateField()
    
    def __str__(self):
        return self.fname