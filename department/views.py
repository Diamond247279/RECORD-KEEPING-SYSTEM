from django.shortcuts import render, redirect
from department.models import Department
from django.urls import reverse
from .forms import DepartmentForm
from django.contrib import messages
# Create your views here.


def welcome(request):
    return render(request, 'department/welcome.html')

def homepage(request):
    departments = Department.objects.all()
    context = {
        'department': departments
    }
    return render(request, 'department/index.html', context)


def new_department(request):
    form = DepartmentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(('new_department'))
    return render(request, 'department/add.html', context)


def delete_department(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, 'DEPARTMENT DELETED')
    return redirect(('homepage'))


def update_department(request, id):
    instance = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None,
                             request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'DEPARTMENT UPDATED')
    return render(request, 'department/update.html', context)


 

