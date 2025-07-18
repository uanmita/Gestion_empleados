from django.urls import path
from . import views

urlpatterns = [
      path('empleados/', views.empleados_list, name='empleados'),
]