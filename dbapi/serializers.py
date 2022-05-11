from rest_framework import serializers
from dbapi.models import Weather, User, Soil, District, Comments, ReplyMessage, PostMessage

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields=('id', 'Name', 'Latitude', 'Longitude')

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields=('id', 'year', 'month', 'day', 'tmin', 'tmax', 'rain')

class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields=('id', 'type', 'ph')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id', 'fname', 'lname', 'email', 'password', 'pnumber')

class PostMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMessage
        fields=('id', 'user', 'message', 'date')

class ReplyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyMessage
        fields=('id', 'PostMessage', 'reply', 'date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields=('id', 'PostMessage', 'reply', 'date')
