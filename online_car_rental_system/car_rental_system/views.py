from django.core import checks
from django.core.checks import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from .models import Car,Customer,IssueCar,Contact,register_table
import random
import os



def create_new_ref_number():
	return str(random.randint(1000,9999))




def home(request):
	return render(request,'index.html')

def about(request):
 	return render(request,'about.html')

def customer(request):
 	return render(request,'customer.html')
def adddetails(request):
	return render(request,'add-details.html')
def searchcar(request):
	return render(request,'search-car.html')
def employee(request):
	return render(request,'employee.html')



def contact(request):
	return render(request,'contact.html')



def caradd(request):
	responseDic = {}
	try:
		# if request.method=="POST":
			# imgs=request.POST['imgs']
			
			car_name= request.POST['car_name']
			car_company = request.POST['car_company']
			car_type = request.POST['car_type']
			car_color = request.POST['car_color']
			car_capacity = request.POST['car_capacity']
			car_number = request.POST['car_number']
			car_fuel = request.POST['car_fuel']
			car_city = request.POST['car_city']
			car_district = request.POST['car_district']
			Car_rent_per_day = request.POST['Car_rent_per_day']
			Status = request.POST['Status']
			if len(request.FILES)!=0:
				imgs=request.FILES['imgs']
			
			carlist = Car(imgs=imgs,car_name=car_name,car_company=car_company,car_type=car_type,car_color=car_color,car_capacity=car_capacity,car_number=car_number,car_fuel=car_fuel,car_city=car_city,car_district=car_district,Car_rent_per_day=Car_rent_per_day,Status=Status)
			carlist.save()
			responseDic["msg1"]="Car Added"
			return render(request, "employee.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="Car Cannot be Added"
		 return render(request, "addcar.html", responseDic)


def adddetails(request):
	try:
		uid=create_new_ref_number()
		first_name= request.POST['first_name']
		last_name = request.POST['last_name']
		address = request.POST['address']
		gender = request.POST['gender']
		dob= request.POST['dob']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		district= request.POST['district']

		cuslist = Customer(uid =uid,first_name=first_name,last_name =last_name ,address=address,gender=gender,dob=dob,email=email,phone_number=phone_number,district=district)
		cuslist.save()
		return render(request, "customer.html")
	
	except Exception as e:
		 print(e)
		 return render(request, "add-details.html")


def viewcar(request):
	cars=Car.objects.all()
	return render(request,"viewcar.html",{'cars':cars})

def delete_data(request,id):
	if request.method =='POST':
		pi=Car.objects.get(pk=id)
		pi.delete()
		return render(request,"employee.html")


def update_data(request,pk):
	prod=Car.objects.get(id=pk)
	if request.method=="POST":
		if len(request.FILES)!=0:
			if len(prod.imgs)>0:
				os.remove(prod.imgs.path)
			prod.imgs=request.FILES['imgs']
		prod.car_name=request.POST['car_name']
		prod.car_company=request.POST['car_company']
		prod.car_type=request.POST['car_type']
		prod.car_color=request.POST['car_color']
		prod.car_capacity=request.POST['car_capacity']
		prod.car_number=request.POST['car_number']
		prod.car_fuel=request.POST['car_fuel']
		prod.car_city=request.POST['car_city']
		prod.car_district=request.POST['car_district']
		prod.Car_rent_per_day =request.POST['Car_rent_per_day']
		prod.Status =request.POST['Status']
		prod.save()
		# messages.succeess(request,"CAR UPDATED")
		return render(request,"employee.html")
			
	context={'prod':prod}
	return render(request,"update.html",context)

#search
def searchcar(request):
	if request.method=="POST":
		car_type=request.POST['name1']
		obj1=Car.objects.filter(car_type=car_type)
		return render(request,'searchcar.html',{'cars':obj1})
		
	else:
		obj2=Car.objects.all()
		return render(request,"searchcar.html",{'cars':obj2})



def issuecar(request):
	responseDic = {}
	try:
		Customername = request.POST['Customername']
		car_name = request.POST['car_name']
		car_company = request.POST['car_company']
		car_type = request.POST['car_type']
		car_color = request.POST['car_color']
		car_capacity = request.POST['car_capacity']
		car_number = request.POST['car_number']
		car_district= request.POST['car_district']
		Car_rent_per_day = request.POST['Car_rent_per_day']
		issuedate = request.POST['issuedate']
		retuendate = request.POST['retuendate']

		carlist = IssueCar(Customername=Customername,car_name=car_name,car_company=car_company,car_type=car_type,car_color=car_color,car_capacity=car_capacity,car_number=car_number,car_district=car_district,Car_rent_per_day=Car_rent_per_day,issuedate=issuedate,retuendate=retuendate)
		carlist.save()
		responseDic["msg1"]="issue car Added"
		return render(request, "employee.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="issue car cannot be Added"
		 return render(request, "issuecar.html", responseDic)


def change_password(request):
	responsiveDic={}
	if request.method=="POST":
		current=request.POST['password']
		new_pass=request.POST['password1']

		user=User.objects.get(id=request.user.id)
		check=user.check_password(current)
		if check==True:
			user.set_password(new_pass)
			user.save()
			responsiveDic["msg"]="Password Change Successfully"
			return redirect('login')
		
		else:
			responsiveDic["msg"]="Incorrect Password"

	return render(request,"registration/change-password.html")

def contact(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		msg=request.POST['msg']

		data=Contact(name=name,email=email,msg=msg)
		data.save()
		res="Dear {} Thanks for Your Feedback".format(name)
		return render(request,'contact.html',{"status":res})
	return render(request,'contact.html')

 
# # Employee	
# def empsignup(request):
# 	if request.method=="POST":
# 		username=request.POST.get('username')
# 		email=request.POST.get('email')
# 		psw=request.POST.get('psw')
# 		repeat_password=request.POST.get('psw-repeat')
# 		user=User.objects.create_user(username=username,email=email,password=psw)
# 		user.save()
# 		print("User Created")
# 		return redirect('emplogin')
# 	else:
# 		return render(request,'registration/empsignup.html')	

# def loginpage(request):
# 	responseDic={}
# 	username = request.POST.get('username')
# 	password = request.POST.get('password')
# 	user = authenticate(request,username=username,password=password)

# 	print(username,password,user)
# 	if user is not None:
# 		login(request,user)
# 		return render(request,'employee.html')
# 	else:
# 		return render(request,'registration/emplogin.html')

# # Customer
		
# def signup_view(request):
# 	if request.method=="POST":
# 		first_name=request.POST.get('first_name')
# 		last_name=request.POST.get('last_name')
# 		username=request.POST.get('username')
# 		email=request.POST.get('email')
# 		password=request.POST.get('psw')
# 		repeat_password=request.POST.get('psw-repeat')
# 		user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
# 		user.save()
# 		print("User Created")
# 		return redirect('login')
# 	else:
# 		return render(request,'registration/signup.html')

# def login_view(request):
# 	return render(request,'registration/login.html')

# def ip_data(request):
# 	responseDic={}
# 	first_name = request.POST.get('first_name')
# 	password_1 = request.POST.get('password_1')
# 	user = authenticate(request,first_name=first_name,password=password_1)

# 	print(first_name,password_1,user)
# 	if user is not None:
# 		login(request,user)
# 		return render(request,'customer.html')
# 	else:
# 		return render(request,'blank.html')


#Edit Customer

def edit_data(request):
	prod=Customer.objects.get(user__username=request.user.username)
	if request.method=="POST":
		prod.username=request.POST['username']
		prod.first_name=request.POST['first_name']
		prod.last_name=request.POST['last_name']
		prod.address=request.POST['address']
		prod.gender=request.POST['gender']
		prod.dob=request.POST['dob']
		prod.email=request.POST['email']
		prod.phone_number=request.POST['phone_number']
		prod.district=request.POST['district']
		prod.save()
		# messages.succeess(request,"CAR UPDATED")
		return render(request,"customer.html")
			
	context={'prod':prod}
	print(prod)
	return render(request,"edit.html.html",context)


#view cust details	
def viewprofile(request):
	return render(request,"profileview.html")	

def register(request):
	if request.method=="POST":
		fname=request.POST["first_name"]
		last=request.POST["last_name"]
		un=request.POST["username"]
		em=request.POST["email"]
		phn=request.POST["phn_number"]
		pwd=request.POST["psw"]
		rpwd=request.POST["psw-repeat"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(username=un,email=em,password=pwd)
		usr.first_name=fname
		usr.last_name=last
		if tp=="employee":
			usr.is_staff=True
		usr.save()
		reg=register_table(user=usr,phone_number=phn)
		reg.save()
		return render(request,"registration.html",{"status":"{} Register Successfully".format(fname)})

	return render(request,"registration.html")

def check_user(request):
	if request.method=="GET":
		un=request.GET["usern"]
		check=User.objects.filter(username=un)
		if len(check)==1:
			return HttpResponse("Exists")
		else:
			return HttpResponse("No Exist")
		

def user_login(request):
	if request.method=="POST":
		un=request.POST["username"]
		ps=request.POST["password"]
		
		user=authenticate(username=un,password=ps)
		if user:
			login(request,user)
			if user.is_superuser: 
				return redirect("/admin")
			if user.is_staff:
				return redirect("customer.html")
			if user.is_active:
				return render(request,"employee.html")


		else:
			return render(request,'user_login.html',{"status":"Invalid User Name or Password"})

	
                        
		