from rest_framework.viewsets import ModelViewSet

from todos.mixins import TodosCacheFlowMixin
from todos.models import Todo
from todos.serializers import TodoSerializer

# Create your views here.


class TodoViewSet(TodosCacheFlowMixin, ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
