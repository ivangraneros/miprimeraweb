from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Entregable
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)