from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('Login')



    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        password = request.POST['password']
        email=request.POST['email']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                            messages.info(request,"User Taken")
                            return redirect('register')
            elif User.objects.filter(email=email).exists():
                            messages.info(request, "email already taken")
                            return redirect('register')
            else:
                            user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email)
                            user.save();
                            print("User Created")

        else:
            messages.info(request,"Password Not matching")
            return redirect('register')
        return (redirect('/'))

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')