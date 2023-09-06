from django.contrib import admin
from .models import Salary, Name, Department

admin.site.register(Salary)
admin.site.register(Department)
admin.site.register(Name)