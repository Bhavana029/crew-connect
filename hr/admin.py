from django.contrib import admin

# Register your models here.
from hr.models import Department, Designation, Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)