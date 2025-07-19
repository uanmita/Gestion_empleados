from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.empleados_list, name='empleados'),
    path('nuevo/', views.empleados_create, name='nuevo'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('', views.index, name='index'),
]