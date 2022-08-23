from dj_drf_utils.action_patterns import STANDARD_PATTERN
from django.urls import path

from . import views

task_view = views.TaskViewSet.as_view(STANDARD_PATTERN)

urlpatterns = [
    path("", task_view),
]
