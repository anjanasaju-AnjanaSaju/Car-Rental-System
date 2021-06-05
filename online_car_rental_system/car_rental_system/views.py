from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
import random


def ref():
	uid=int(random.randint(111,999))
	return uid 


def home(request):
	return render(request,'index.html')

def about(request):
 	return render(request,'about.html')
def login(request):
	return render(request,'registration/login.html')
def contact(request):
	return render(request,'contact.html')
# sign up

def signup(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		user_name=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('psw')
		repeat_password=request.POST.get('psw-repeat')
		user=User.objects.create_user(username=user_name,password=password,email=email,first_name=first_name)
		user.save()
		print("User Created")
		return redirect('login')

	else:
		return render(request,'registration/signup.html')

