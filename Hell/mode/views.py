from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from mode.models import Register
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
 


# Create your views here.

def index(request):
    return render(request,"index.html")
def terms(request):
    return render(request,"terms.html")    
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact = Contact(name= name ,email=email,desc=desc) 
        contact.save() 
        messages.success(request, 'Your message has been sent!')  
    return render(request,"contact.html")     
def loginusr(request):
    if request.method == "POST":
        password1=request.POST.get('password1')
        email1=request.POST.get('email1')
        print(password1,email1)

        if Register.objects.filter(email=email1).exists():
            if Register.objects.filter(password=password1).exists():
                messages.info(request,"Hello Welcome to Our website")
                return render(request,"index.html")
            else:
                messages.info(request,"Password are not matching !")
                return redirect("/register")    
        else:
            messages.info(request,"invalid credentials Register yourself (:")    
            return redirect("/register")


    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')

        if password==confirm_password:
            if Register.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
            else:
                register=Register(first_name=first_name,last_name=last_name,email=email,password=password,confirm_password=confirm_password)
                register.save()
                messages.info(request,"you are registered successfully!")
                      
        else:
            messages.info(request,"password are not matching")
            return redirect("/register")
       

        
         
    return render(request,"register.html")                                                                                                                    