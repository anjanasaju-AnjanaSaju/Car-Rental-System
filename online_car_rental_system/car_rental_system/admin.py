from django.contrib import admin
from .models import Customer, Employee,Car, Car_Booking
from .models import User

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    search_fields=('Employee_name','join_city','join_district')
admin.site.register(Employee,EmployeeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    search_fields=('first_name','booking_date')
admin.site.register(Customer,CustomerAdmin)

class CarAdmin(admin.ModelAdmin):
    search_fields=('car_name','	car_company','car_type','car_color','car_capacity','car_number','car_fuel','car_city','car_district','Car_rent_per_day')
admin.site.register(Car,CarAdmin)

admin.site.register(Car_Booking)