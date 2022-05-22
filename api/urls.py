from django.urls import path, re_path as url
from .views import *

urlpatterns = [
    path('rain/', RainPrediction.as_view(), name = 'rain_prediction'), 
    path('rainDE/', RainPrediction_DE.as_view(), name = 'Debre Elias rain prediction'), 
    path('rainYJ/', RainPrediction_YJ.as_view(), name = 'Yejubie rain prediction'),    
    path('harvestrain/', HarvestRainPrediction.as_view(), name = 'Harvest rain_prediction'), 
    path('harvestrainDE/', HarvestRainPrediction_DE.as_view(), name = 'Debre Elias Harvest rain prediction'), 
    path('harvestrainYJ/', HarvestRainPrediction_YJ.as_view(), name = 'Yejubie Harvest rain prediction'),        
]