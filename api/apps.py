import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'api'    
    MODEL_FILE = os.path.join(settings.MODELS, "MainDS.joblib")
    MODEL_FILE2 = os.path.join(settings.MODELS, "MainDS2.joblib")
    MODEL_FILE3 = os.path.join(settings.MODELS, "MainDS3.joblib")
    model = joblib.load(MODEL_FILE)
    model2 = joblib.load(MODEL_FILE2)
    model3 = joblib.load(MODEL_FILE3)