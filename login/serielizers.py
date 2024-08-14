from rest_framework.serializers import ModelSerializer
from login.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"