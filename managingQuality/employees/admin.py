from django.contrib import admin

# Register your models here.

from .forms import EmployeeForm

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'last_name', 'email', 'phone')

    form = EmployeeForm


    #class Meta:
     #   model = Employee


admin.site.register(Employee, EmployeeAdmin)
