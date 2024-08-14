from django.shortcuts import render
from drf_spectacular.utils import extend_schema,extend_schema_view
from rest_framework import viewsets

from login.serielizers import TaskSerializer
from login.models import Task

@extend_schema_view(
    list=extend_schema(description="Permite obtner una lista de tareas"),
    retrive=extend_schema(description="Permite obtener una tarea"),
    create=extend_schema(description="Permite Crear una Tarea"),
    update=extend_schema(description="Permite editar una Tarea"),
    destroy=extend_schema(description="Permite eliminar una Tarea")
)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
