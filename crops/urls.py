# crops/urls.py
from django.urls import path
from .views import CropRecommendation

urlpatterns = [
    path('api/recommend-crops/<str:location>/', CropRecommendation.as_view(), name='recommend-crops')
]