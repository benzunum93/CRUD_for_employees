from django.contrib import admin

import employee_register
from .models import Employee, Position

# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)