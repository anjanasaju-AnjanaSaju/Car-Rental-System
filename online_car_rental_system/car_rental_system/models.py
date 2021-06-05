from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Employee(models.Model):
	Employee_name=models.CharField(max_length=100)
	user_name=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	join_city=models.CharField(max_length=50)
	join_district=models.CharField(max_length=50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	

	def __str__(self):
		return self.Employee_name


class Customer(models.Model):
	uid=models.CharField(
		max_length=10,
		blank=True,
		editable=False,
		unique=True,
		)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	user_name=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	gender=models.CharField(max_length=50)
	dob=models.DateField()
	email=models.CharField(max_length=50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	district=models.CharField(max_length=50)
	booking_date=models.DateField()
	total_no_of_days=models.IntegerField()
	payment=models.IntegerField()


	def __str__(self):
		return self.first_name


class Car(models.Model):
	car_name=models.CharField(max_length=100)
	car_company=models.CharField(max_length=100)
	car_type=models.CharField(max_length=100)
	car_color=models.CharField(max_length=100)
	car_capacity=models.IntegerField()
	car_number=models.CharField(max_length=50)
	car_fuel=models.CharField(max_length=100)
	car_city=models.CharField(max_length=100)
	car_district=models.CharField(max_length=100)
	Car_rent_per_day=models.IntegerField()
	
	def __str__(self):
		return self.car_name


class Car_Booking(models.Model):
	uid=models.IntegerField()
	customer_name=models.CharField(max_length=100)
	car_name=models.CharField(max_length=100)
	Car_rent_per_day=models.IntegerField()
	total_no_of_days=models.IntegerField()
	total_amount=models.IntegerField()
	advance_amount=models.IntegerField()
	balance_amount=models.IntegerField()


	def __str__(self):
		return self.customer_name
	






