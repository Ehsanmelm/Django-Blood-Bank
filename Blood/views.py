from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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
    # serializer_class = BloodRequest_Serializer
    # queryset = BloodRequestModel.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = BloodRequestModel.objects.all()
        else:
            authenticated_user_id = self.request.user.id
            queryset = BloodRequestModel.objects.filter(
                Q(requested_patient_id=authenticated_user_id) | Q(requested_donor_id=authenticated_user_id))
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_staff:
            return BloodRequest_For_admin_Serializer
        return BloodRequest_Serializer

    def get_serializer_context(self):
        try:
            patient = patientModel.objects.get(
                patient_id=self.request.user.id)
            # donor, donor_created = patientModel.objects.get_or_create(
            #     donor_id=self.request.user.id)
            if patient:
                return {'requested_patient_id': self.request.user.id, 'requested_donor_id': None}
        except:
            return
        # if donor:
            # return
        # if get_object_or_404()

    # @action(detail=False, methods=['GET', 'POST'])
    # def Request(self, request):

        # class Blood_requests_view(ModelViewSet):
        #     queryset = BloodRequestModel.objects.all()
        #     serializer_class = BloodRequest_Serializer
    def put(self, request, pk):
        blood_request = BloodRequestModel.objects.get(id=pk)
        data = request.data
        requested_bloodtype = BloodModel.objects.get(
            bloodtype=data['bloodtype'])
        status = data['status']

        blood_request.reason = data['reason']
        blood_request.unit = data['unit']
        blood_request.bloodtype = data['bloodtype']

        if status.lower() == 'accept':
            if requested_bloodtype.unit - data['unit'] >= 0:
                blood_request.unit = requested_bloodtype.unit - data['unit']
                requested_bloodtype.save()
            else:
                blood_request.status = 'Denied'

        blood_request.save()
        # blood_request.bloodtype = data['bloodtype']
