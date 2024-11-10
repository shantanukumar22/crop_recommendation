# from django.contrib import admin
# from .models import Crop

# admin.site.register(Crop)
# crops/admin.py
from django.contrib import admin
from .models import Crop

class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'crop_type', 'ideal_temperature_min', 'ideal_temperature_max', 'ideal_rainfall_min', 'ideal_rainfall_max', 'ideal_soil_type']
    search_fields = ['name', 'crop_type']
    list_filter = ['crop_type', 'ideal_soil_type']

admin.site.register(Crop, CropAdmin)