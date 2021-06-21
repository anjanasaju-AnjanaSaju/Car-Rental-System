from django.contrib import admin
from django.contrib import auth
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
path('',views.home,name="home"),

# path('accounts/login/ip_data',views.ip_data), 
# path('accounts/login',views.login_view, name="login"),

# path('accounts/signup/',views.signup_view, name="signup"),
 
# path('accounts/emplogin/',views.loginpage,name="emplogin"),
# path('accounts/empsignup/',views.empsignup, name="empsignup"),
path("signup/",views.register,name="reg"),
path("user_login/",views.user_login,name="user_login"),
path("check_user/",views.check_user,name="check_user"),
path('about',views.about,name="about"),
path('contact',views.contact,name="contact"),
path('customer',views.customer,name="customer"),
path('add-details',views.adddetails,name="add-details"),
path('searchcar',views.searchcar,name="search-car"),
path('employee',views.employee,name="employee"),
path('addcar',views.caradd,name="addcar"),
path('viewcar',views.viewcar,name="viewcar"),
path('delete/<int:id>/',views.delete_data,name="deletedata"),
path('updatedata/<str:pk>/',views.update_data,name="updatedata"),
path('searchcar',views.searchcar,name="searchcar"),
path('issuecar',views.issuecar,name="issuecar"),
path('accounts/change_password/',views.change_password,name="change_password"),
# path('editdata',views.edit_data,name="editdata"),
path('viewprofile',views.viewprofile,name="viewprofile"),
path('accounts/login/login',views.user_login),
path('viewissue',views.viewissue,name="viewissue"),
path('deleteissue/<int:id>/',views.deleteissue,name="delete_data"),

]	


