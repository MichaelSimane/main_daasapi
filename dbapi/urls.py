from django.urls import path, re_path as url
from .views import *
from dbapi import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [      
    url(r'^district$', views.DistrictApi),
    url(r'^district/([0-9]+)$', views.DistrictApi),    

    url(r'^weather$', views.WeatherApi),
    url(r'^weather/([0-9]+)$', views.WeatherApi),
    path('weatherdetail/<int:year>/<int:month>/<int:day>/<str:district>', views.WeatherDetailApi), 
    path('WeatherDetailReportApi/<int:year>/<int:month>/<str:district>', views.WeatherDetailReportApi),    

    url(r'^soil$', views.SoilApi),
    url(r'^soil/([0-9]+)$', views.SoilApi),  
    path('soildetail/<str:district>', views.SoilDetailApi),   

    url(r'^user$', views.UserApi),
    url(r'^user/([0-9]+)$', views.UserApi),    

    url(r'^postmessage$', views.PostMessageApi),
    url(r'^postmessage/([0-9]+)$', views.PostMessageApi),    

    url(r'^replymessage$', views.ReplyMessageApi),
    url(r'^replymessage/([0-9]+)$', views.ReplyMessageApi),    

    url(r'^comment$', views.CommentsApi),
    url(r'^comment/([0-9]+)$', views.CommentsApi), 

    url(r'^analyzed$', views.AnalyzedDataApi),
    url(r'^analyzed/([0-9]+)$', views.AnalyzedDataApi), 

    url(r'^weather/savefile$', views.SaveFileApi),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)