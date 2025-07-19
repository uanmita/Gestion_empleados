from django.shortcuts import render
from .models import Empleado, GestionPortfolios


def index(request):
    return render(request, 'empleados/index.html')

def empleados_list(request):
    empleados = Empleado.objects.select_related('departamento').all()  # Agregué .all()
    return render(request, 'empleados/list.html', {'empleados': empleados})

def empleados_create(request):
   return render(request, 'empleados/new.html')

def portfolio_list(request):
    proyectos = GestionPortfolios.objects.all()
    return render(request, 'empleados/portfolio.html', {'proyectos': proyectos})