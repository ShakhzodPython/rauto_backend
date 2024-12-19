from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', CarCategoryAPIView.as_view(), name='car_category'),
    path('body-type/', BodyTypeAPIView.as_view(), name='body_type'),
    path('fuel-type/', TypeFuelAPIView.as_view(), name='type_fuel'),
    path('gearbox/', GearboxAPIView.as_view(), name='gearbox'),
    path('machine-condition/', MachineConditionAPIView.as_view(), name='machine_condition'),
    path('machine-drive/', MachineDriveAPIView.as_view(), name='machine_drive'),
    path('color/', ColorAPIView.as_view(), name='color'),
    path('', HomeCarListAPIView.as_view(), name='home_car'),
    path('<int:pk>/', CarDetailAPIView.as_view(), name='car_detail'),
    path('add/', CreateCarAPIView.as_view(), name='create_car'),
]
