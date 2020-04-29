from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUS = (
        (0,"InActive"),
        (1,"Active")
)
class Role(models.Model):
    ADMIN = 1
    MANAGER =2
    USER = 3
    ROLE_CHOICES = [
        (ADMIN, 'ADMIN'),
        (MANAGER, 'MANAGER'),
        (USER, 'USER'),
    ]
    role = models.CharField(
        max_length=11,
        default='USER'
    )

    def is_admin(self):
        if self.role == 1:
            return 1
    def is_manger(self):
        if self.role == 2:
            return 1
    def is_employee(self):
        if self.role == 3:
            return 1
    def __str__(self):
       return self.role


class User(AbstractUser):
     roles = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)

class Department(models.Model):
    name = models.CharField(max_length=11)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    idno = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    passwordbkp = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = "media/")
    phone = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    idno = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    managerid = models.ForeignKey(Manager, on_delete=models.CASCADE)
    passwordbkp = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = "images/")
    phone = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Leavetype(models.Model):
    leavetype = models.CharField(max_length=255)
    limit = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class Leave(models.Model):
    reference =  models.ForeignKey(User, on_delete=models.CASCADE)
    leavetype = models.ForeignKey(Leavetype, on_delete=models.CASCADE)
    leavestart = models.DateTimeField()
    leaveend = models.DateTimeField()
    reason = models.TextField()
    subject = models.CharField(max_length=255)
    comment = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    reference =  models.ForeignKey(User, on_delete=models.CASCADE)
    timein = models.CharField(max_length=255)
    timeout = models.CharField(max_length=255)
    totalhour = models.CharField(max_length=255)
    statustimein = models.CharField(max_length=255)
    statustimeout = models.CharField(max_length=255)
    reason = models.TextField()
    comment = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class EmployeeNotice(models.Model):
    title =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class ManagerNotice(models.Model):
    title =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


