from rest_framework.viewsets import ModelViewSet

from tasks.mixins import TasksCacheFlowMixin
from tasks.serializers import TaskSerializer

from .models import Task

# Create your views here.


class TaskViewSet(TasksCacheFlowMixin, ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
