# from django.db import models

# class Crop(models.Model):
#     name = models.CharField(max_length=100)
#     ideal_temperature_min = models.FloatField()
#     ideal_temperature_max = models.FloatField()
#     ideal_rainfall_min = models.FloatField()
#     ideal_rainfall_max = models.FloatField()

#     def __str__(self):
#         return self.name
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=50, default="Unknown")  # Default value for crop_type
    ideal_temperature_min = models.FloatField()  # Ideal min temperature
    ideal_temperature_max = models.FloatField()  # Ideal max temperature
    ideal_rainfall_min = models.FloatField()  # Min rainfall required
    ideal_rainfall_max = models.FloatField()  # Max rainfall required
    ideal_soil_type = models.CharField(max_length=100, default="Loamy")  # Default value for soil_type
    humidity_level = models.CharField(max_length=100, default="50")  # Default value for humidity_level
    pesticides_required = models.TextField(default="None")  # Default value for pesticides_required
    special_care = models.TextField(default="None")  # Default value for special_care
    government_policies = models.TextField(default="No policies available")  # Default value for government_policies
    ideal_sunlight = models.CharField(max_length=100, default="Full Sun")  # Default value for ideal_sunlight
    soil_moisture_level = models.CharField(max_length=100, default="Moderate")  # Default value for soil_moisture_level
    recommended_pesticides = models.TextField(default="None")  # Default value for recommended_pesticides

    def __str__(self):
        return self.name