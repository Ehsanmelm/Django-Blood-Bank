from rest_framework import serializers
from .models import BloodModel, BloodRequestModel
from . import views
from patient.models import patientModel


class BloodRequest_Serializer(serializers.ModelSerializer):
    requested_patient_id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = BloodRequestModel
        fields = ['id', 'requested_patient_id', 'reason',
                  'unit', 'bloodtype', 'status', 'date']

    def create(self, validated_data):
        patient_id = self.context['requested_patient_id']
        if patient_id:
            return BloodRequestModel.objects.create(
                requested_patient_id=patient_id,  **validated_data)


class BloodRequest_For_admin_Serializer(serializers.ModelSerializer):
    requested_patient_id = serializers.IntegerField(read_only=True)
    status = serializers.CharField()

    class Meta:
        model = BloodRequestModel
        fields = ['id', 'requested_patient_id', 'reason',
                  'unit', 'bloodtype', 'status', 'date']

    def create(self, validated_data):
        patient_id = self.context['requested_patient_id']
        if patient_id:
            return BloodRequestModel.objects.create(
                requested_patient_id=patient_id,  is_patient=True, **validated_data)


class BloodManaging_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BloodModel
        fields = ['id', 'blood', 'unit']

    def save(self, **kwargs):
        blood_type = self.validated_data['blood']
        unit = self.validated_data['unit']
        try:
            blood_info = BloodModel.objects.get(blood=blood_type)
            blood_info.unit += unit
            blood_info.save()
            self.instance = blood_info
        except BloodModel.DoesNotExist:
            self.instance = BloodModel.objects.create(
                unit=unit, blood=blood_type)
        return self.instance
