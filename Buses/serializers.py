from rest_framework import serializers
from Buses.models import CurrentLocation

class CurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLocation
        fields = ('license_plate', 'lattitude', 'longitude', 'passengers')
