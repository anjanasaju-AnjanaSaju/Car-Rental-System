from django.contrib import admin
from .models import Customer, Employee,Car_Booking,IssueCar,Car,Payment,Contact,register_table
from .models import User

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    search_fields=('Employee_name','join_city','join_district')
admin.site.register(Employee,EmployeeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    search_fields=('first_name',)
admin.site.register(Customer,CustomerAdmin)

class CarAdmin(admin.ModelAdmin):
    search_fields=('car_name','	car_company','car_type','car_color','car_capacity','car_number','car_fuel','car_city','car_district','Car_rent_per_day')
admin.site.register(Car,CarAdmin)

admin.site.register(Car_Booking)

class IssueCarAdmin(admin.ModelAdmin):
    search_fields=('issuedate','returndate')
admin.site.register(IssueCar,IssueCarAdmin)

class PaymentAdmin(admin.ModelAdmin):
    search_fields=('payment_status',)
admin.site.register(Payment,PaymentAdmin)

class ContactAdmin(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(Contact,ContactAdmin)

admin.site.register(register_table)