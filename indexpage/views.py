from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import feature, contactus
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
                myuser.save()
                return redirect('login')
        else:
            messages.info(request,'The password is not same')
            return redirect('registration')         
    else:
        return render(request,'regis.html')

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Please enter valid Credentials')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    if request.method =="POST":
        contact=contactus()
        name=request.POST.get('name1')
        email=request.POST.get('email1')
        subject=request.POST.get('subject1')
        message=request.POST.get('message1')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1> thanks for contacting us</h1>")
    return render(request,'contact.html')

def booking(request):
    if request.method=="POST":
        book=booking()
        name=request.POST.get('name')
        email=request.POST.get('email')
        bookingT=reques.POST.get('bookingT')
        people=request.POST.get('people')
        req=request.POST.get('request1')
        book.name=name
        book.email=email
        book.booking_time=bookingT
        book.people=people
        book.req=req
        book.save()
        return  render(request,'menu.html')
    return render(request,'booking.html')