from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from adminpanel.models import User,Employee,Manager,Department,Leavetype,Role
from django.db import transaction


STATUS =( 
    ("1", "Active"), 
    ("2", "InActive"),  
) 
class EmployeeForm(UserCreationForm):
    
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': "form-control"}), help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"}))
    birthday = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    passwordbkp = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), required=False, help_text='Optional.')
    avatar = forms.ImageField()
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args,**kwargs)
    class Meta:
        model = User
        fields = ['username']
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.roles_id = 3
        user.save()
        employee = Employee.objects.create(user=user)
        employee.name.add(*self.cleaned_data.get('name'))
        employee.phone.add(*self.cleaned_data.get('phone'))
        employee.department.add(*self.cleaned_data.get('department'))
        employee.birthday.add(*self.cleaned_data.get('birthday'))
        employee.passwordbkp.add(*self.cleaned_data.get('passwordbkp'))
        employee.avatar.add(*self.cleaned_data.get('avatar'))
        return user

class ManagerForm(UserCreationForm):
    
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}), required=True, help_text='Optional.')
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
        fields = ['username']
        

    
    def save(self,*args,**kwargs commit=True):
        user = super(ManagerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.roles_id = 3
            user.save()
        return user


class DepartmentForm(ModelForm):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':"form-control",'id':"simpleinputname"}), required=False)
    status = forms.ChoiceField(choices = STATUS, label='Manager', widget=forms.Select(attrs={'class' :"form-control" ,'data-plugin':"customselect"})) 
    class Meta:
        model = Department
        fields = ('name', 'status')