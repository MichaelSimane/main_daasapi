import statistics
from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dbapi.models import *
from dbapi.serializers import *

from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def DistrictApi(request, id=0):
    if request.method == 'GET':
        district = District.objects.all()
        district_serializer = DistrictSerializer(district, many=True)
        return JsonResponse(district_serializer.data, safe=False)
    elif request.method == 'POST':
        district_data = JSONParser().parse(request)
        district_serializer = DistrictSerializer(data=district_data)
        if district_serializer.is_valid():
            district_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        district_data = JSONParser().parse(request)
        district = District.objects.get(id = id)
        district_serializer = DistrictSerializer(district, data=district_data)
        if district_serializer.is_valid():
            district_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        district = District.objects.get(id = id)
        district.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def WeatherApi(request, id=0):
    if request.method == 'GET':
        weather = Weather.objects.all()
        weather_serializer = WeatherSerializer(weather, many=True)
        return JsonResponse(weather_serializer.data, safe=False)
    elif request.method == 'POST':
        weather_data = JSONParser().parse(request)
        weather_serializer = WeatherSerializer(data=weather_data)
        if weather_serializer.is_valid():
            weather_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        weather_data = JSONParser().parse(request)
        weather = Weather.objects.get(id = id)
        weather_serializer = WeatherSerializer(weather, data=weather_data)
        if weather_serializer.is_valid():
            weather_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        weather = Weather.objects.get(id = id)
        weather.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def WeatherDetailApi(request, district, year, month, day):
    try:
        district = District.objects.get(Name=district)
        weather = Weather.objects.get(year=year, month=month, day=day, district=district.id)
        tmean = float((weather.tmin + weather.tmax) / 2)
    except Weather.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        return JsonResponse(tmean, safe=False)

@csrf_exempt
def WeatherDetailReportApi(request, district, year, month):
    try:
        district = District.objects.get(Name=district)
        
        weather = Weather.objects.filter(year=year, month__range=[month, month+1], district=district.id)
        weather_serializer = WeatherSerializer(weather, many=True)        
    except Weather.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        return JsonResponse(weather_serializer.data, safe=False)

@csrf_exempt
def SoilApi(request, id=0):
    if request.method == 'GET':
        soil = Soil.objects.all()
        soil_serializer = SoilSerializer(soil, many=True)
        return JsonResponse(soil_serializer.data, safe=False)
    elif request.method == 'POST':
        soil_data = JSONParser().parse(request)
        soil_serializer = SoilSerializer(data=soil_data)
        if soil_serializer.is_valid():
            soil_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        soil_data = JSONParser().parse(request)
        soil = Soil.objects.get(id = id)
        soil_serializer = SoilSerializer(soil, data=soil_data)
        if soil_serializer.is_valid():
            soil_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        soil = Soil.objects.get(id = id)
        soil.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SoilDetailApi(request, district):
    try:
        district = District.objects.get(Name=district)        
        soil = Soil.objects.get(district=district.id)
        soil_serializer = SoilSerializer(soil)        
    except Weather.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

    if request.method == 'GET':        
        return JsonResponse(soil_serializer.data, safe=False)
@csrf_exempt
def UserApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id = id)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(id = id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def PostMessageApi(request, id=0):
    if request.method == 'GET':
        postmessage = PostMessage.objects.all()
        postmessage_serializer = PostMessageSerializer(postmessage, many=True)
        return JsonResponse(postmessage_serializer.data, safe=False)
    elif request.method == 'POST':
        postmessage_data = JSONParser().parse(request)
        postmessage_serializer = PostMessageSerializer(data=postmessage_data)
        if postmessage_serializer.is_valid():
            postmessage_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        postmessage_data = JSONParser().parse(request)
        postmessage = PostMessage.objects.get(id = id)
        postmessage_serializer = PostMessageSerializer(postmessage, data=postmessage_data)
        if postmessage_serializer.is_valid():
            postmessage_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        postmessage = PostMessage.objects.get(id = id)
        postmessage.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def GetPostMessageApi(request, id):
    try:
        post = PostMessage.objects.get(id=id)        
    except Weather.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        postmessage_serializer = PostMessageSerializer(data=post)       
        return JsonResponse(postmessage_serializer, safe=False)

@csrf_exempt
def ReplyMessageApi(request, id=0):
    if request.method == 'GET':
        replymessage = ReplyMessage.objects.all()
        replymessage_serializer = ReplyMessageSerializer(replymessage, many=True)
        return JsonResponse(replymessage_serializer.data, safe=False)
    elif request.method == 'POST':
        replymessage_data = JSONParser().parse(request)
        replymessage_serializer = ReplyMessageSerializer(data=replymessage_data)
        if replymessage_serializer.is_valid():
            replymessage_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        replymessage_data = JSONParser().parse(request)
        replymessage = ReplyMessage.objects.get(id = id)
        replymessage_serializer = ReplyMessageSerializer(replymessage, data=replymessage_data)
        if replymessage_serializer.is_valid():
            replymessage_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        replymessage = ReplyMessage.objects.get(id = id)
        replymessage.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def CommentsApi(request, id=0):
    if request.method == 'GET':
        comment = Comments.objects.all()
        comment_serializer = CommentSerializer(comment, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comment = Comments.objects.get(id = id)
        comment_serializer = CommentSerializer(comment, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        comment = Comments.objects.get(id = id)
        comment.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def AnalyzedDataApi(request, id=0):
    if request.method == 'GET':
        analyzed = AnalyzedData.objects.all()
        analyzed_serializer = AnalyzedDataSerializer(analyzed, many=True)
        return JsonResponse(analyzed_serializer.data, safe=False)
    elif request.method == 'POST':
        analyzed_data = JSONParser().parse(request)
        analyzed_serializer = AnalyzedDataSerializer(data=analyzed_data)
        if analyzed_serializer.is_valid():
            analyzed_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        analyzed_data = JSONParser().parse(request)
        analyzed = AnalyzedData.objects.get(id = id)
        analyzed_serializer = AnalyzedDataSerializer(analyzed, data=analyzed_data)
        if analyzed_serializer.is_valid():
            analyzed_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        analyzed = AnalyzedData.objects.get(id = id)
        analyzed.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFileApi(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


