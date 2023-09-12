from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


# Define the FileViewSet class
class FileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = File.objects.all()
    serializer_class = FileSerializer


# Define the file_count function-based view
@api_view(["GET"])
@csrf_exempt  # If CSRF protection is not required
@permission_classes([IsAuthenticated])  # Add appropriate permissions
def file_count(request):
    queryset = File.objects.all()
    count = queryset.count()
    return Response({"count": count}, status=status.HTTP_200_OK)
