from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
# Create your views here.
class MyCustomLogin(auth_views.LoginView):
    redirect_authenticated_user =True


 
