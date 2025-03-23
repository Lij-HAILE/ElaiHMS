from django.contrib import admin
from .models import MyUser
from django.contrib.auth import admin as base

from .forms import UserUpdateForm,CreateUserForm
# Register your models here.
@admin.register(MyUser)
class MyuserAdmin(base.UserAdmin):
    form =UserUpdateForm
    add_form = CreateUserForm
    list_display= ('username','role')
    fieldsets = (('personal',{"fields":('username',"password")}),(None,{"fields":('role',)}))