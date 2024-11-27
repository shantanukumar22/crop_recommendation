# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import requests
# from .models import Crop

# class CropRecommendation(APIView):
#     def get(self, request, location):
#         # Get weather data for the location
#         weather_data = self.get_weather_data(location)
        
#         if "error" in weather_data:
#             return Response({"error": weather_data["error"]}, status=status.HTTP_400_BAD_REQUEST)

#         # Use weather data to recommend crops
#         recommended_crops = self.recommend_crops(weather_data)
#         return Response({"recommended_crops": recommended_crops}, status=status.HTTP_200_OK)

#     def get_weather_data(self, location):
#         api_key = "a47cf057af008c975c6ff3c42eccf21c"  # Replace with your API key
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#         response = requests.get(url)
#         weather_data = response.json()
#         print("Weather Data:", weather_data)  # Debugging line
#         return weather_data
#         # Debug: Print the weather data to check its contents
#         print(weather_data)

#         if response.status_code != 200:
#             return {"error": "Could not fetch weather data or invalid location"}

#         return weather_data

#     def recommend_crops(self, weather_data):
#         temperature = weather_data['main']['temp']
#         rainfall = weather_data.get('rain', {}).get('1h', 0)

#         # Debug: Print the weather conditions
#         print(f"Temperature: {temperature}, Rainfall: {rainfall}")

#         crops = Crop.objects.all()
#         recommended_crops = []

#         for crop in crops:
#             print(f"Checking crop: {crop.name}")  # Debug: Check each crop
#             if crop.ideal_temperature_min <= temperature <= crop.ideal_temperature_max and \
#                crop.ideal_rainfall_min <= rainfall <= crop.ideal_rainfall_max:
#                print(f"Adding {crop.name} to recommended crops")
#                recommended_crops.append(crop.name)

#         return recommended_crops
#!
# # crops/views.py
# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Crop

# class CropRecommendation(APIView):
#     def get(self, request, location):
#         # Get weather data for the location
#         weather_data = self.get_weather_data(location)
        
#         # Recommend crops based on weather data
#         recommended_crops = self.recommend_crops(weather_data)
        
#         # Return the response with additional crop data
#         response_data = []
#         for crop in recommended_crops:
#             crop_data = {
#                 'name': crop.name,
#                 'crop_type': crop.crop_type,
#                 'ideal_temperature': f"{crop.ideal_temperature_min}°C to {crop.ideal_temperature_max}°C",
#                 'ideal_rainfall': f"{crop.ideal_rainfall_min}mm to {crop.ideal_rainfall_max}mm",
#                 'humidity': crop.humidity_level,
#                 'soil_type': crop.ideal_soil_type,
#                 'special_care': crop.special_care,
#                 'government_policies': crop.government_policies,
#                 'recommended_pesticides': crop.recommended_pesticides,
#                 'soil_moisture_level': crop.soil_moisture_level,
#                 'ideal_sunlight': crop.ideal_sunlight
#             }
#             response_data.append(crop_data)

#         return Response(response_data, status=status.HTTP_200_OK)

#     def get_weather_data(self, location):
#         api_key = "a47cf057af008c975c6ff3c42eccf21c"  # Replace with your OpenWeather API key
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {}

#     def recommend_crops(self, weather_data):
#         temperature = weather_data['main']['temp'] if 'main' in weather_data else 0
#         rainfall = weather_data.get('rain', {}).get('1h', 0)  # Get rainfall data
        
#         crops = Crop.objects.all()
#         recommended_crops = []
#         for crop in crops:
#             if crop.ideal_temperature_min <= temperature <= crop.ideal_temperature_max and \
#                crop.ideal_rainfall_min <= rainfall <= crop.ideal_rainfall_max:
#                 recommended_crops.append(crop)

#         return recommended_crops

# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from .models import Crop

# # CropRecommendation API to recommend crops based on location weather
# class CropRecommendation(APIView):
#     def get(self, request, location):
#         # Get weather data for the location
#         weather_data = self.get_weather_data(location)
        
#         if not weather_data:
#             return Response({"error": "Could not fetch weather data for the location."}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Recommend crops based on weather data
#         recommended_crops = self.recommend_crops(weather_data)
        
#         # Return the response with additional crop data
#         response_data = []
#         for crop in recommended_crops:
#             crop_data = {
#                 'name': crop.name,
#                 'crop_type': crop.crop_type,
#                 'ideal_temperature': f"{crop.ideal_temperature_min}°C to {crop.ideal_temperature_max}°C",
#                 'ideal_rainfall': f"{crop.ideal_rainfall_min}mm to {crop.ideal_rainfall_max}mm",
#                 'humidity': crop.humidity_level,
#                 'soil_type': crop.ideal_soil_type,
#                 'special_care': crop.special_care,
#                 'government_policies': crop.government_policies,
#                 'recommended_pesticides': crop.recommended_pesticides,
#                 'soil_moisture_level': crop.soil_moisture_level,
#                 'ideal_sunlight': crop.ideal_sunlight
#             }
#             response_data.append(crop_data)

#         return Response(response_data, status=status.HTTP_200_OK)

#     def get_weather_data(self, location):
#         api_key = "a47cf057af008c975c6ff3c42eccf21c"  # Replace with your OpenWeather API key
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {}

#     def recommend_crops(self, weather_data):
#         temperature = weather_data['main']['temp'] if 'main' in weather_data else 0
#         rainfall = weather_data.get('rain', {}).get('1h', 0)  # Get rainfall data
        
#         crops = Crop.objects.all()
#         recommended_crops = []
#         for crop in crops:
#             if crop.ideal_temperature_min <= temperature <= crop.ideal_temperature_max and \
#                crop.ideal_rainfall_min <= rainfall <= crop.ideal_rainfall_max:
#                 recommended_crops.append(crop)

#         return recommended_crops


# # Crop details API to fetch details of a specific crop
# def crop_details(request, crop_name):
#     try:
#         # Get the crop based on the name
#         crop = Crop.objects.get(name__iexact=crop_name)
#         data = {
#             'name': crop.name,
#             'crop_type': crop.crop_type,
#             'ideal_temperature': crop.ideal_temperature_max,
#             'humidity': crop.humidity,
#             'soil_type': crop.soil_type,
#             'special_care': crop.special_care,
#             'government_policies': crop.government_policies,
#             'recommended_pesticides': crop.recommended_pesticides,
#             'soil_moisture_level': crop.soil_moisture_level,
#             'ideal_sunlight': crop.ideal_sunlight,
#         }
#         return JsonResponse(data)
#     except Crop.DoesNotExist:
#         return JsonResponse({'error': 'Crop not found'}, status=404)


import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Crop

# CropRecommendation API to recommend crops based on location weather
class CropRecommendation(APIView):
    def get(self, request, location):
        # Get weather data for the location
        weather_data = self.get_weather_data(location)
        
        if not weather_data:
            return Response({"error": "Could not fetch weather data for the location."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Recommend crops based on weather data
        recommended_crops = self.recommend_crops(weather_data)
        
        # Return the response with additional crop data
        response_data = []
        for crop in recommended_crops:
            crop_data = {
                'name': crop.name,
                'crop_type': crop.crop_type,
                'ideal_temperature': f"{crop.ideal_temperature_min}°C to {crop.ideal_temperature_max}°C",  # Show both min and max temperature
                'ideal_rainfall': f"{crop.ideal_rainfall_min}mm to {crop.ideal_rainfall_max}mm",  # Show both min and max rainfall
                'humidity': crop.humidity_level,  # Corrected field name
                'soil_type': crop.ideal_soil_type,
                'special_care': crop.special_care,
                'government_policies': crop.government_policies,
                'recommended_pesticides': crop.recommended_pesticides,
                'soil_moisture_level': crop.soil_moisture_level,
                'ideal_sunlight': crop.ideal_sunlight
            }
            response_data.append(crop_data)

        return Response(response_data, status=status.HTTP_200_OK)

    def get_weather_data(self, location):
        api_key = "a47cf057af008c975c6ff3c42eccf21c"  # Replace with your OpenWeather API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Return the weather data if successful
        else:
            return {}  # Return an empty dictionary if the request fails

    def recommend_crops(self, weather_data):
        temperature = weather_data['main']['temp'] if 'main' in weather_data else 0
        rainfall = weather_data.get('rain', {}).get('1h', 0)  # Get rainfall data, defaulting to 0 if not available
        
        crops = Crop.objects.all()
        recommended_crops = []
        for crop in crops:
            if crop.ideal_temperature_min <= temperature <= crop.ideal_temperature_max and \
               crop.ideal_rainfall_min <= rainfall <= crop.ideal_rainfall_max:
                recommended_crops.append(crop)

        return recommended_crops


# Crop details API to fetch details of a specific crop
def crop_details(request, crop_name):
    try:
        # Get the crop based on the name (case-insensitive search)
        crop = Crop.objects.get(name__iexact=crop_name)
        data = {
            'name': crop.name,
            'crop_type': crop.crop_type,
            'ideal_temperature': f"{crop.ideal_temperature_min}°C to {crop.ideal_temperature_max}°C",  # Combine min and max temperatures
            'ideal_rainfall': f"{crop.ideal_rainfall_min}mm to {crop.ideal_rainfall_max}mm",  # Combine min and max rainfall
            'humidity': crop.humidity_level,  # Corrected field name
            'soil_type': crop.ideal_soil_type,
            'special_care': crop.special_care,
            'government_policies': crop.government_policies,
            'recommended_pesticides': crop.recommended_pesticides,
            'soil_moisture_level': crop.soil_moisture_level,
            'ideal_sunlight': crop.ideal_sunlight
        }
        return JsonResponse(data)
    except Crop.DoesNotExist:
        return JsonResponse({'error': 'Crop not found'}, status=404)