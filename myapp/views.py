from django.contrib import messages
from django.shortcuts import redirect, render
from . models import LoginTable,UserProfile
from . forms import LoginTableForm,UserProileForm
# Create your views here.

def login(request):
    return render(request,'login.html')

def userRegistration(request):
    logintable = LoginTable()
    userprofile = UserProfile()
    
    userform=UserProileForm()
    
    if request.method == 'POST':
        logintable.username = request.POST.get('username')
        logintable.password = request.POST.get('password')
        logintable.password2 = request.POST.get('password2')
        logintable.type = 'user'
        userprofile.username = request.POST.get('username')
        userprofile.password = request.POST.get('password')
        userprofile.password2 = request.POST.get('password2')
        if logintable.password == logintable.password2:
            logintable.save()
            userprofile.save()
            messages.info(request,'user created successfully please login')
            return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
       
    
    return render(request,'register.html',{'userform':userform})