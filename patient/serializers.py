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
    # requests = serializers.HyperlinkedRelatedField(
    #     queryset=BloodRequestModel.objects.filter(
    #         requested_patient_id=patient_id),
    #     serializers=Patient_BloodRequest_Serializer
    # )

    def create(self, validated_data):
        patient_id = self.context['patient_id']
        return patientModel.objects.create(patient_id=patient_id,  **validated_data)
