from rest_framework import serializers
from .models import DonorModel, DonateRequestModel


class DonorSerializer(serializers.ModelSerializer):
    donor_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = DonorModel
        fields = ['id', 'donor_id', 'profile_pic',
                  'bloodtype', 'age', 'mobile', 'address']

    def create(self, validated_data):
        donor_id = self.context['donor_id']
        return DonorModel.objects.create(donor_id=donor_id, **validated_data)


class DonateRequest_Serializer(serializers.ModelSerializer):
    requested_donor_id = serializers.IntegerField(read_only=True)
    date = serializers.DateField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = DonateRequestModel
        fields = ['id', 'requested_donor_id', 'disease',
                  'bloodtype', 'unit', 'date', 'status']

    def create(self, validated_data):
        donor_id = self.context['donor_id']
        return DonateRequestModel.objects.create(
            requested_donor_id=donor_id, **validated_data)


class DonateRequest_Serializer_4Admin(serializers.ModelSerializer):
    requested_donor_id = serializers.IntegerField(read_only=True)
    date = serializers.DateField(read_only=True)

    class Meta:
        model = DonateRequestModel
        fields = ['id', 'requested_donor_id', 'disease',
                  'bloodtype', 'unit', 'date', 'status']

    def create(self, validated_data):
        donor_id = self.context['donor_id']
        return DonateRequestModel.objects.create(
            requested_donor_id=donor_id, **validated_data)
