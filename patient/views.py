from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import patientModel
from .serializers import PatientSerializer

# Create your views here.


class PatientViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return patientModel.objects.all()
        return patientModel.objects.filter(patient_id=self.request.user.id)

    def get_serializer_context(self):
        return {'patient_id': self.request.user.id}
