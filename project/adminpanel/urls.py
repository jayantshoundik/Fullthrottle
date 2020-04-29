from django.urls import path

from adminpanel import views

urlpatterns = [
     path('dashboard',views.index,name = 'dashboard'),
     path('login/',views.login,name = 'login'),
     path('employee/add',views.addEmployee,name = 'employeeadd'),
     path('manager/add',views.addManager,name = 'manageradd'),
     path('department',views.addDepartment,name = 'department'),
     path('logout/',views.logout,name = 'logout'),

]