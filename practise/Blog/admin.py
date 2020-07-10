from django.contrib import admin

# Register your models here.
from .models import Student,Company
admin.site.register(Student)
admin.site.register(Company)