from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.


def home(request):

    myform = EmployeeForm()
    if (request.POST):
        savedform = EmployeeForm(request.POST)
        if(savedform.is_valid()):
            savedform.save()
    context = {

        "EmployeeForm": myform,
    }


    return render(request, "index.html", context)
