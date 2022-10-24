# from email import message
# from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from study.forms import UserRegisterForm

# Create your views here.

def home(request):
    return render(request,'index.html',{'name':'Shantanu'})

# User registration function
def register_fun(request):
    # get values by post methods
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        u_name=request.POST.get('u_name')

        if User.objects.filter(username=u_name).exists():
            messages.error(request,"Username already taken . Try different")
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already present. Try different")
            return redirect('register')

        elif pass1!=pass2:
            messages.error(request,"Password not matching")
            return redirect('register')

        else:            
            user=User.objects.create(username=u_name, first_name=f_name, last_name=l_name, email=email, password=pass1)
            user.save()
            user.set_password(pass1)
            user.save()
            messages.success(request,"Registered Successfully")
            print("\n registration successful!!\n")
            return redirect('login')

    return render(request,'register.html')



# login functionality
def login_fun(request):
    # flag for checking login page
    flag=True

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print("login success")
            login(request,user)
            return redirect('/')
        else:
            print("\n login failed\n")
            messages.error(request,"Invalid credentials")
            return redirect('login')

    return render(request,'register.html', {'flag':flag})


# logout function
def logout_fun(request):
    logout(request)
    return redirect('home')


