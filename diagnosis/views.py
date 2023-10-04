from .models import Diagnosis
from rest_framework import viewsets, permissions
from .serializers import DiagnosisSerializer

# Create your views here.
class DiagnosisViewSet(viewsets.ModelViewSet):
    #Main Query For the Index Route
    queryset = Diagnosis.objects.all()
    #Serializer class for serializing output
    serializer_class = DiagnosisSerializer
    permission_classes = [permissions.AllowAny]