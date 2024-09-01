from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == "POST":
        user_name = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(user_name,email,password)
        myuser.save()
        return redirect('loginn')
    return render (request,'signup.html')


def loginn(request):
    if request.method == "POST":
        user_name = request.POST['Username']
        password = request.POST['password']
    
        user=authenticate(username=user_name,password=password)

        if user is not None:
            login(request,user)

            return redirect('index')
        else:
            return redirect('signup')
    return render (request,'login.html')


def index(request):
    return render (request,'crud.html')