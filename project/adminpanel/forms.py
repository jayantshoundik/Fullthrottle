from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from adminpanel.models import User,Department,Leavetype,Role
from django.db import transaction


STATUS =( 
    ("1", "Active"), 
    ("2", "InActive"),  
) 
class EmployeeForm(UserCreationForm):
    
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': "form-control"}), help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"}))
    birthday = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    passwordbkp = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    manager = forms.ModelChoiceField(queryset=User.objects.all(), label='Manager', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"}))
    avatar = forms.ImageField()
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args,**kwargs)
    class Meta:
        model = User
        fields = ['username']
        

    @transaction.atomic
    def save(self,commit=True):
        user = super(EmployeeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            userrole = Role.objects.filter(role = 'EMPLOYEE')
            user.roles = userrole
            assign_manager = self.cleaned_data.get('manager')
            user_manager = User.objects.get(name=assign_manager)
            user.manager = user_manager
            assign_department = self.cleaned_data.get('department')
            user_department = Department.objects.get(name=assign_department)
            user.department = user_department
            user.save()  
        return user

class ManagerForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': "form-control"}), help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"}))
    birthday = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    passwordbkp = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    avatar = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name']
    @transaction.atomic
    def save(self,commit=True):
        user = super(ManagerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            userrole = Role.objects.filter(role = 'MANAGER')
            user.roles = userrole
            assign_department = self.cleaned_data.get('department')
            user_department = Department.objects.get(name=assign_department)
            user.department = user_department
            user.save()
            
        return user


class DepartmentForm(ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control",'id':"simpleinputname"}), required=False)
    status = forms.ChoiceField(choices = STATUS, label='Manager', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"})) 
    class Meta:
        model = Department
        fields = ('name', 'status')
    def __str__(self):
        return self.name

class LeaveTypeForm(ModelForm):
    leavetype = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':"form-control",'id':"simpleinputname"}), required=False)
    limit = forms.IntegerField( widget=forms.TextInput(attrs={'class':"form-control",'id':"simpleinputname"}), required=False)
    status = forms.ChoiceField(choices = STATUS, label='Status', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"})) 
    class Meta:
        model = Leavetype
        fields = ('leavetype', 'limit','status')
    def __str__(self):
        return self.name