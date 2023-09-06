from django.shortcuts import render
from .models import Salary
from django.http import HttpResponse
from .forms import EmployeeForm


def emp_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = EmployeeForm()

    return render(request, 'register/emp_form.html', {'form': form})
