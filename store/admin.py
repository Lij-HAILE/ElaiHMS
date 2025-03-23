from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('customer',"pieces","complete")
@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ('user',"title")
@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    list_display = ('user',"date")
@admin.register(Table)
class tableAdmin(admin.ModelAdmin):
    list_display=('name',)