from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from .models import BloodModel, BloodRequestModel
from patient.models import patientModel
from .serializers import BloodManaging_Serializer, BloodRequest_Serializer, BloodRequest_For_admin_Serializer
from patient.serializers import PatientSerializer

# Create your views here.


class BloodManaging_View(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = BloodModel.objects.all()
    serializer_class = BloodManaging_Serializer


class BloodRequestView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = BloodRequestModel.objects.all()
        else:
            authenticated_user_id = self.request.user.id
            queryset = BloodRequestModel.objects.filter(
                Q(requested_patient_id=authenticated_user_id))
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_staff:
            return BloodRequest_For_admin_Serializer
        return BloodRequest_Serializer

    def get_serializer_context(self):
        try:
            patient = patientModel.objects.get(
                patient_id=self.request.user.id)

            if patient:
                return {'requested_patient_id': self.request.user.id}
        except:
            return {}

    def update(self, request, pk):

        is_admin = self.request.user.is_staff
        blood_request = BloodRequestModel.objects.get(id=pk)
        data = request.data
        requested_bloodtype = BloodModel.objects.get(
            blood=data['bloodtype'])
        if is_admin:
            status = data['status']
        else:
            status = 'Pending'
        if blood_request.status.lower() != 'accept':
            blood_request.reason = data['reason']
            blood_request.unit = data['unit']
            blood_request.bloodtype = data['bloodtype']
            print(status)
            if status.lower() == 'accept':
                if requested_bloodtype.unit - int(data['unit']) >= 0:
                    requested_bloodtype.unit = requested_bloodtype.unit - \
                        int(data['unit'])
                    blood_request.status = status
                    requested_bloodtype.save()
                else:
                    blood_request.status = 'Denied'
                    raise APIException("There is not  enough blood!")
        elif status.lower() == 'denied':
            blood_request.status = 'Denied'

        blood_request.save()
        if is_admin:
            serializer = BloodRequest_For_admin_Serializer(blood_request)
        else:
            serializer = BloodRequest_Serializer(blood_request)
        return Response(serializer.data)
