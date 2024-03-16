from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.email


class parties(models.Model):
    name=models.CharField(max_length=300)
    ppic=models.ImageField(upload_to='static/parties',default="")
    pdate=models.DateField()

class signup(models.Model):
    aadhar=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=15)
    mobile=models.CharField(max_length=20)
    picture=models.ImageField(upload_to='static/profile',default="")
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    passwd=models.CharField(max_length=200)
    age=models.IntegerField()


class upcomingelction(models.Model):
    etitle=models.CharField(max_length=100)
    edes=models.TextField(max_length=5000)
    edate=models.DateField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.etitle


class vote(models.Model):
    aadhar=models.CharField(max_length=20)
    vparty=models.CharField(max_length=20)
    vdate=models.DateField()



