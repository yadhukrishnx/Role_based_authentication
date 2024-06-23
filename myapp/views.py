from django.contrib import messages
from django.shortcuts import redirect, render
from . models import LoginTable,UserProfile

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=LoginTable.objects.filter(username = username,password = password).exists()
        try:
            if user is not None:
                user_details=LoginTable.objects.get(username = username,password=password)
                user_name=user_details.username
                type=user_details.type
                if type=='user':
                    request.session['username']=user_name
                    return redirect('home')
                elif type=='admin':
                    request.session['username']=user_name
                    return redirect('adminhome')   
            else:
                messages.error(request,'invalid credentials')
        except:
            messages.error(request,'invalid role')
    return render(request,'login.html')

def userRegistration(request):
    logintable = LoginTable()
    userprofile = UserProfile()
    

    
    if request.method == 'POST':
        logintable.username = request.POST.get('username')
        logintable.password = request.POST.get('password')
        logintable.password2 = request.POST.get('password2')
        logintable.type = 'user'
        userprofile.username = request.POST.get('username')
        userprofile.password = request.POST.get('password')
        userprofile.password2 = request.POST.get('password2')
        if logintable.password == logintable.password2:
            if LoginTable.objects.filter(username = logintable.username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            logintable.save()
            userprofile.save()
            messages.info(request,'user created successfully please login')
            return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
       
    
    return render(request,'register.html')

def home(request):
    user_name= request.session['username']
    return render(request,'home.html',{'user_name':user_name})

def adminhome(request):
    
    return render(request,'adminhome.html')