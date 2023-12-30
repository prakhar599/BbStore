from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import Author , Blog, ContactMessage
from .forms import signUpForm, logInForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.core.paginator import Paginator



def index(request):
     blogs = Blog.objects.all().order_by('name')
     paginator = Paginator(blogs,6,orphans=3) # Show 25 contacts per page.
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     return render(request,'blog/blog.html',{'page_obj':page_obj})

def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created successfully.')
            return redirect('/blog/login')
        else:
            # Add form errors to messages
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.warning(request, f"{field}: {error}")
            return redirect('/blog/signup')
    else:
        form = signUpForm()
    return render(request,'blog/signup.html',context = {'form':form})


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get("username", False)
        password1 = request.POST.get("password")
        user = authenticate(request , username = username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            return render(request,'blog/failure.html')
    else:
        form = logInForm()
        return render(request,'blog/login.html',context = {'form':form})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('txt_name')
        email = request.POST.get('txt_email')
        phone = request.POST.get('txt_phone')
        subject = request.POST.get('txt_subject')
        message = request.POST.get('txt_message')

        # Save the contact message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return render(request, 'blog/thank_you.html')
    return render(request, 'blog/contact.html')



def logout(request):
    auth_logout(request)
    return redirect('/blog')

def create_Blog(request):
    return render(request,'blog/newBlog.html')

def read_Blog(request,myid):
    blog = Blog.objects.filter(id=myid)
    return render(request,'blog/blogcontent.html',{'blog':blog[0]})

def update_Blog(request):
    return render(request,'blog/updateBlog.html')

def about_Us(request):
    return render(request,'blog/aboutus.html')

def books(request):
    return render(request,'blog/books.html')

