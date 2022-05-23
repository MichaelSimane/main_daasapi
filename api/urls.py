from django.urls import path, re_path as url
from .views import *

urlpatterns = [
    path('Debre Markos/', RainPrediction.as_view(), name = 'rain_prediction'), 
    path('Debre Elias/', RainPrediction_DE.as_view(), name = 'Debre Elias rain prediction'), 
    path('Yejube/', RainPrediction_YJ.as_view(), name = 'Yejubie rain prediction'),    
    path('harvest_Debre Markos/', HarvestRainPrediction.as_view(), name = 'Harvest rain_prediction'), 
    path('harvest_Debre Elias/', HarvestRainPrediction_DE.as_view(), name = 'Debre Elias Harvest rain prediction'), 
    path('harvest_Yejube/', HarvestRainPrediction_YJ.as_view(), name = 'Yejubie Harvest rain prediction'),        
]