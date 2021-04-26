from django.contrib import admin

# Register your models here.
from .models import Employee, AvailableJobs


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id','phone_num']


@admin.register(AvailableJobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']