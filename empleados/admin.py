from django.contrib import admin
from .models import Empleado, Departamento, GestionPortfolios


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'departamento')
    list_filter = ('departamento',)

admin.register(Departamento)
admin.site.register(GestionPortfolios)