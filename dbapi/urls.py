from django.urls import path, re_path as url
from .views import *
from dbapi import views

urlpatterns = [      
    url(r'^district$', views.DistrictApi),
    url(r'^district/([0-9]+)$', views.DistrictApi),    

    url(r'^weather$', views.WeatherApi),
    url(r'^weather/([0-9]+)$', views.WeatherApi),    

    url(r'^soil$', views.SoilApi),
    url(r'^soil/([0-9]+)$', views.SoilApi),    

    url(r'^user$', views.UserApi),
    url(r'^user/([0-9]+)$', views.UserApi),    

    url(r'^postmessage$', views.PostMessageApi),
    url(r'^postmessage/([0-9]+)$', views.PostMessageApi),    

    url(r'^replymessage$', views.ReplyMessageApi),
    url(r'^replymessage/([0-9]+)$', views.ReplyMessageApi),    

    url(r'^comment$', views.CommentsApi),
    url(r'^comment/([0-9]+)$', views.CommentsApi),    
]