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
