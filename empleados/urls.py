from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.empleados_list, name='empleados'),
    path('nuevo/', views.empleados_create, name='nuevo'),
    path('', views.index, name='index'),
]