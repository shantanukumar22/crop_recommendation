from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ['id', 'name', 'ideal_temperature_min', 'ideal_temperature_max', 'ideal_rainfall_min', 'ideal_rainfall_max']