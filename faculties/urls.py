from django.urls import path

from .views import (
    FacultyCreateAPIView,
    FacultyDetailAPIView,
)

urlpatterns = [
    path( "create/", FacultyCreateAPIView.as_view(), name="faculty-list-create"),
    path("<int:pk>/", FacultyDetailAPIView.as_view(),name="faculty-detail"),
]