from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    """
    this function forregister
    """
    form = UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1==password2:
                # we can chech the length and strong of password,but we ignor
                User.objects.create_user(username=username,email=email,password=password1)
                # login user
                user=authenticate(username=username,password=password1)
                login(request,user)
                return redirect('roshan:dataset_view')
            else:
                messages.error(request,'password not match')
        else:
            return HttpResponse("invalid or weak password")
    else:
        return  render(request,'register/register.html',{'form':form})    

def login_view(request):
    """
    this function for login
    """
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if  form.is_valid():
            user_name=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=user_name,password=password)
            if user  is not None :
                login(request,user)
                messages.info(request, f"You are now logged in as {user_name}.")
                # return redirect('roshan:dataset_view')
                return redirect(request.GET.get('next','/'))
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form=AuthenticationForm()
    return render(request,'register/login.html',{'form':form}) 
        
@login_required
def logout_view(request):
    """
    this function for logout
    """
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect("blog:blog_list")

@login_required
def delete_account(request,id):
    """
    this function for delete oprator account
    """
    user=User.objects.get(id=id)
    if request.method=="POST":
        user.delete()
        messages.success(request,"Account Deleted Successfully")
        return redirect('roshan:dataset_view')
    return render(request,'register/delete_account.html',{"user":user}) 
