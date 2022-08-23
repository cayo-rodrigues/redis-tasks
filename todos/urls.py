from dj_drf_utils.action_patterns import STANDARD_PATTERN
from django.urls import path

from . import views

todo_view = views.TodoViewSet.as_view(STANDARD_PATTERN)

urlpatterns = [
    path("", todo_view),
]
