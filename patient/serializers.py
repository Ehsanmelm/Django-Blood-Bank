from rest_framework import serializers
from .models import patientModel
from Blood.models import BloodRequestModel
# from Blood.serializers import Patient_BloodRequest_Serializer


class PatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = patientModel
        fields = ['id', 'patient_id', 'profile_pic', 'age',
                  'bloodtype', 'disease', 'address', 'mobile']

    def create(self, validated_data):
        patient_id = self.context['patient_id']
        return patientModel.objects.create(patient_id=patient_id,  **validated_data)
