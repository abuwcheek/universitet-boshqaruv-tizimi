from django.urls import path

from .views import (
    TaskListCreateAPIView,
    TaskDetailAPIView,
    TeacherTaskStatusAPIView,
    MyTaskListAPIView,
)


urlpatterns = [
    path("", TaskListCreateAPIView.as_view(), name="task-list-create"),

    path("<int:pk>/status/", TeacherTaskStatusAPIView.as_view(), name="teacher-task-status"),    ##tasklarni statusini o'zgartirish uchun endpoint

    path("my/", MyTaskListAPIView.as_view(), name="my-tasks"),

    path("<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
]