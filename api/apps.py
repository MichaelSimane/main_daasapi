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
    HARVEST_MODEL_FILE = os.path.join(settings.MODELS, "HarvestDS.joblib")
    HARVEST_MODEL_FILE2 = os.path.join(settings.MODELS, "HarvestDS2.joblib")
    HARVEST_MODEL_FILE3 = os.path.join(settings.MODELS, "HarvestDS3.joblib")
    harvestmodel = joblib.load(HARVEST_MODEL_FILE)
    harvestmodel2 = joblib.load(HARVEST_MODEL_FILE2)
    harvestmodel3 = joblib.load(HARVEST_MODEL_FILE3)