from rest_framework import serializers
from . import models
from .models import Position, Employee


class PositionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Position
		fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta: 
    	model = Employee
    	fields = '__all__'


