from dj_drf_utils.action_patterns import STANDARD_DETAIL_PATTERN, STANDARD_PATTERN
from django.urls import path

from . import views

todo_view = views.TodoViewSet.as_view(STANDARD_PATTERN)
todo_detail_view = views.TodoViewSet.as_view(STANDARD_DETAIL_PATTERN)

urlpatterns = [
    path("", todo_view),
    path("<pk>/", todo_detail_view),
]
