from django.urls import path
from .views import RainPrediction, RainPrediction_DE, RainPrediction_YJ

urlpatterns = [
    path('rain/', RainPrediction.as_view(), name = 'rain_prediction'), 
    path('rainDE/', RainPrediction_DE.as_view(), name = 'Debre Elias rain prediction'), 
    path('rainYJ/', RainPrediction_YJ.as_view(), name = 'Yejubie rain prediction')    
]