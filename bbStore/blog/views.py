from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect 
from .models import Author , Blog
from .forms import signUpForm, logInForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate,login

def index(request):
    context = {
        'blogs' : Blog.objects.all().order_by('name')
    }
    return render(request,'blog/blog.html',context)

def blog(request):
    context = {
        'blogs' : Blog.objects.all().order_by('name')
    }
    return render(request,'blog/blog.html',context)
 
 
def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST) 
        if form.is_valid():
            form.save() 
        if form.errors :
            print('hi')
            messages.warning(request,' Incorrect Credentials')
            return redirect('/blog/signup',form.errors)  
        messages.success(request,'account created successfully.')
        return render(request,'blog/success.html',{'form': form })
        
    else:
        form = signUpForm()             
    return render(request,'blog/signup.html',context = {'form':form})  
 

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get("username", False)
        password1 = request.POST.get("password1")       
        # user = authenticate(request , username = username, password1=password1,password2=password2)
        user = authenticate(request , username = username, password=password1)

        if user is not None:
            login(request, user)
            messages.success(request,'logging in successful !')
            return render(request,'blog/login.html')  
        else:
            messages.warning(request,' Incorrect Credentials or account does not exist')
            return render(request,'blog/failure.html') 
               
    else:
        form = logInForm()     
        return render(request,'blog/login.html',context = {'form':form})


def create_Blog(request):
    return render(request,'blog/newBlog.html')

def read_Blog(request,myid):
    blog = Blog.objects.filter(id=myid)
    return render(request,'blog/blogContent.html',{'blog':blog[0]})

def update_Blog(request):
    return render(request,'blog/updateBlog.html')

def contact_Us(request):
    return render(request,'blog/contact.html')

def about_Us(request):
    return render(request,'blog/aboutus.html')

def books(request):
    return render(request,'blog/books.html')    
    
