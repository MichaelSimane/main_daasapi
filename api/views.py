from django.shortcuts import render
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RainPrediction(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']        
        model = ApiConfig.model  

        rain_predicted = model.predict([[year, month, day, tmax]])  
        
        return Response(rain_predicted, status=200)

class RainPrediction_DE(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']  
        model2 = ApiConfig.model2
               
        rain_predicted2 = model2.predict([[year, month, day, tmax]]) 
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted2, status=200)

class RainPrediction_YJ(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']
        model3 = ApiConfig.model3           
        rain_predicted3 = model3.predict([[year, month, day, tmax]])          
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted3, status=200)

class HarvestRainPrediction(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmin = data['tmin']  
        tmax = data['tmax']        
        harvestmodel = ApiConfig.harvestmodel  

        rain_predicted = harvestmodel.predict([[year, month, day, tmin, tmax]])  
        
        return Response(rain_predicted, status=200)

class HarvestRainPrediction_DE(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmin = data['tmin']
        tmax = data['tmax']  
        harvestmodel2 = ApiConfig.harvestmodel2
               
        rain_predicted2 = harvestmodel2.predict([[year, month, day, tmin, tmax]]) 
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted2, status=200)

class HarvestRainPrediction_YJ(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmin = data['tmin']
        tmax = data['tmax']
        harvestmodel3 = ApiConfig.harvestmodel3           
        rain_predicted3 = harvestmodel3.predict([[year, month, day, tmin, tmax]])          
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted3, status=200)

class LocustPrediction(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']        
        locust = ApiConfig.model  

        locust_predicted = locust.predict([[year, month, day, tmax]])  
        
        return Response(locust_predicted, status=200)

class LocustPrediction_DE(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']  
        locust2 = ApiConfig.locust2
               
        locust_predicted2 = locust2.predict([[year, month, day, tmax]]) 
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(locust_predicted2, status=200)

class LocustPrediction_YJ(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']
        locust3 = ApiConfig.locust3           
        locust_predicted3 = locust3.predict([[year, month, day, tmax]])          
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(locust_predicted3, status=200)





