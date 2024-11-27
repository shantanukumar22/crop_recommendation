# # crops/urls.py
# from django.urls import path
# from .views import CropRecommendation

# urlpatterns = [
#     path('api/recommend-crops/<str:location>/', CropRecommendation.as_view(), name='recommend-crops')
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Route for getting crop details by name
    path('api/crop-details/<str:crop_name>/', views.crop_details, name='crop_details'),
    
    # Route for recommending crops based on location
    path('api/recommend-crops/<str:location>/', views.CropRecommendation.as_view(), name='crop_recommendation'),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # URL for fetching crop details by name
#     path('api/crop-details/<str:crop_name>/', views.crop_details, name='crop_details'),
    
#     # URL for getting crop recommendations based on location
#     path('api/recommend-crops/<str:location>/', views.CropRecommendation.as_view(), name='crop_recommendation'),
# ]