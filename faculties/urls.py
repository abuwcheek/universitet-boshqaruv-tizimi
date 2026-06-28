from django.urls import path

from .views import (
    FacultyListCreateAPIView,
    FacultyDetailAPIView,
)

urlpatterns = [
    path( "", FacultyListCreateAPIView.as_view(), name="faculty-list-create"),
    path("<int:pk>/", FacultyDetailAPIView.as_view(),name="faculty-detail"),
]