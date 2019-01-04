from django.contrib import admin
from .models import User, ConfirmString
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','sex','c_time')
@admin.register(ConfirmString)
class ConfirmStringAdmin(admin.ModelAdmin):
    list_display = ('code','user','c_time')