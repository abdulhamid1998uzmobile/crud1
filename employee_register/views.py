from django.shortcuts import render,redirect
from .form import EmployeeForm
from .models import Employee
from rest_framework import viewsets
from employee_register.models import Position,Employee
from employee_register.serializers import PositionSerializer,EmployeeSerializer

class PositionViewSet(viewsets.ModelViewSet):
	queryset = Position.objects.all()
	serializer_class = PositionSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
# Create your views here.
def employee_list(request):
	context = {"employee_list":Employee.objects.all()}
	return render(request,"employee_register/employee_list.html",context)

def employee_form(request, id=0):
	if request.method =="GET":
		if id==0:
			form = EmployeeForm()
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(instance=employee)	
		return render(request,"employee_register/employee_form.html",{'form':form})
	else:
		if id==0:
			form = EmployeeForm(request.POST)
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/employee/list')	

def employee_delete(request,id):
	employee = Employee.objects.get(pk=id)
	employee.delete()
	return redirect('/employee/list')	
	