from django.urls import path
from tasks.views import (
    TaskListView, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagCreateView, TagUpdateView, TagDeleteView, task_change_done_status_view,
)


app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/change_done_status/",
         task_change_done_status_view,
         name="task_change_done_status"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
