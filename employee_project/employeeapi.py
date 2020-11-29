from rest_framework import routers
from employee_register import views
router = routers.DefaultRouter()
router.register(r'positions',views.PositionViewSet)
router.register(r'employee',views.EmployeeViewSet)