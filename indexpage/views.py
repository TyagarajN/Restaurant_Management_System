from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def registration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exists')
                return redirect('registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exists')
                return redirect('registration')
            else:
                myuser = User.objects.create_user(username=username,first_name=fname,last_name=lastname,email=email,password=password)
                myuser.first_name = fname
                myuser.lastname = lastname
                myuser.email = email
                myuser.password = password
                myuser.save()
                return redirect('login')
        else:
            messages.info(request,'The password is not same')
            return redirect('registration')         
    else:
        return render(request,'regis.html')

def login(request):
    return render(request, 'login.html')