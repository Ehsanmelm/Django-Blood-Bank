from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import DonorModel, DonateRequestModel
from Blood.models import BloodModel
from .serializers import DonorSerializer, DonateRequest_Serializer, DonateRequest_Serializer_4Admin
# Create your views here.


class DonorView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = DonorModel.objects.all()
        else:
            queryset = DonorModel.objects.filter(donor_id=self.request.user.id)
        return queryset
    serializer_class = DonorSerializer

    def get_serializer_context(self):
        return {'donor_id': self.request.user.id}


class DonateRequestView(ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_staff:
            return DonateRequestModel.objects.all()
        else:
            # print(DonateRequestModel.objects.all().donor__donor__username)
            return DonateRequestModel.objects.filter(requested_donor_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return DonateRequest_Serializer_4Admin
        else:
            return DonateRequest_Serializer

    def get_serializer_context(self):
        return {'donor_id': self.request.user.id}

    def update(self, request, pk, *args, **kwargs):
        is_admin = self.request.user.is_staff
        donate_request = DonateRequestModel.objects.get(id=pk)
        donating_blood_type = BloodModel.objects.get(blood=data['bloodtype'])
        data = request.data

        if is_admin:
            status = data['status']
        else:
            status = 'Pending'

        if donate_request.status.lower() != 'accept':
            donate_request.disease = data['disease']
            donate_request.unit = data['unit']
            donate_request.bloodtype = data['bloodtype']
            if data['status'].lower() == 'accept':
                donating_blood_type.unit += data['unit']
                donating_blood_type.save()
            else:
                donate_request.status = 'Denied'
        donate_request.save()

        if is_admin:
            serializer = DonateRequest_Serializer_4Admin(donate_request)
        else:
            serializer = DonateRequest_Serializer(donate_request)
        return Response(serializer.date)
