from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
# Create your views here.
def home(req):
    pdata=parties.objects.all()

    return render(req,'user/index.html',{"p":pdata})

def about(req):
    return render(req,'user/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        a=request.POST.get("name","")
        b=request.POST.get("mobile","")
        c=request.POST.get("email","")
        d=request.POST.get("msg","")
        x=contact(name=a,email=c,contact=b,message=d)
        x.save()
        status=True
        #return HttpResponse("<script>alert('Thanks for enquiry..');window.location.href='/user/contactus/'</script>")

    return render(request,'user/contactus.html',{'S':status})

def services(req):
    return render(req,'user/services.html')

def myorders(req):
    return render(req,'user/myorders.html')

def myprofile(req):
    return render(req,'user/myprofile.html')

def product(req):
    return render(req,'user/product.html')

def registration(request):
    if request.method=='POST':
        aadhar=request.POST.get("aadhar","")
        name=request.POST.get("name","")
        gen=request.POST.get("gender","")
        mobile=request.POST.get("mobile","")
        a=request.FILES['rpic']
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        age=request.POST.get("age","")
        passwd=request.POST.get("pwd","")
        a=signup.objects.filter(aadhar=aadhar).count()>0
        if a==True:
            return HttpResponse("<script>alert('You are already registered..');window.location.href='/user/register/'</script>")
        else:
            signup(aadhar=aadhar,name=name,gender=gen,mobile=mobile,picture=a,city=city,state=state,passwd=passwd,age=age).save()
            return HttpResponse("<script>alert('You are registered successfully..');window.location.href='/user/register/'</script>")

    return render(request,'user/registrations.html')

def uelection(request):
    edata=upcomingelction.objects.all().order_by('-id')


    return render(request,'user/uelection.html',{"data":edata})

def login(request):
    if request.method=="POST":
        aadharno=request.POST.get('aadhar')
        passwd=request.POST.get('password')
        data=signup.objects.filter(aadhar=aadharno,passwd=passwd)
        if data.count()>0:

            request.session['aadhar']=aadharno
            return HttpResponse("<script>alert('Thanks for login');window.location.href='/user/vote';</script>")
        else:

            return HttpResponse("<script>alert('Your Aadhar no or Password are incorrect...');window.location.href='/user/login';</script>")

    return render(request,'user/login.html')

def voteforparty(request):
    vdata=parties.objects.all()
    aadharno=request.session.get('aadhar')
    if request.method=="POST":
        a=request.POST.get('vote','')
        checkvoter = vote.objects.filter(aadhar=aadharno).count()
        if checkvoter>0:
            return HttpResponse("<script>alert('You are already atemped..');window.location.href='/user/home/';</script>")
        else:
            vote(aadhar=aadharno,vparty=a,vdate=datetime.datetime.now()).save()
            return HttpResponse("<script>alert('Thanks for vote..');window.location.href='/user/home/';</script>")

        #vote(aadhar=aadharno,vparty=a,vdate=datetime.datetime.now()).save()


    return render(request,'user/voteforparty.html',{"party":vdata})

