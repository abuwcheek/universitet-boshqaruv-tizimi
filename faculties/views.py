from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrRektorOrViceRektor
from .models import Faculty
from .serializers import FacultySerializer



class FacultyCreateAPIView(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated, IsAdminOrRektorOrViceRektor]


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.is_active = True  # Set is_active to True by default
        self.perform_create(serializer)
        data = {
            "message": "Fakultet muvaffaqiyatli yaratildi.",
            "faculty": serializer.data,
            "status": status.HTTP_201_CREATED
        }
        return Response(data)



class FacultyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer