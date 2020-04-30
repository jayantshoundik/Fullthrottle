from django.shortcuts import render,redirect
from django.http import HttpResponse
from project.decorators  import admin_required
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from adminpanel.models import User,Department,Leavetype,Role
from adminpanel.forms import EmployeeForm,DepartmentForm,ManagerForm,LeaveTypeForm

# Create your views here.

@admin_required
def index(request):
    return render(request,'adminpanel/index.html')
@admin_required
def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.department = request.department
            form.save()  
    else:
        form = EmployeeForm()
    return render(request, 'adminpanel/addemployee.html', {'form': form})

@admin_required
def addManager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST,request.FILES)
        if form.is_valid():
            
            form.save()  
    else:
        form = ManagerForm()
    return render(request, 'adminpanel/addmanager.html', {'form': form})

@admin_required
def addDepartment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = DepartmentForm()
    departments = Department.objects.all() 
    return render(request, 'adminpanel/department.html', {'form': form,'departments':departments})


@admin_required
def leaveType(request):
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = LeaveTypeForm()
    leavetypes = Leavetype.objects.all() 
    return render(request, 'adminpanel/leavetype.html', {'form': form,'leavetypes':leavetypes})

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
   
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        
        if user is not None and user.roles_id == 1:
            auth_login(request, user)
            return redirect('dashboard')
    return render(request,'adminpanel/login.html')
@admin_required
def logout(request):
    auth_logout(request)
    return redirect("login")


