from datetime import date
from django.db import models

# Create your models here.
class District(models.Model):
    Name = models.CharField(max_length=64)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return f"{self.id} {self.Name} {self.Latitude} {self.Longitude}"


class Weather(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    year = models.IntegerField(max_length=64)
    month = models.IntegerField(max_length=64)
    day = models.IntegerField(max_length=128)
    tmin = models.FloatField() 
    tmax = models.FloatField() 
    rain = models.FloatField() 
    district = models.ForeignKey(District, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.id} {self.year} {self.month} {self.day} {self.tmin} {self.tmax} {self.rain} {self.district}"

class Soil(models.Model):
    type = models.CharField(max_length=10)
    ph = models.FloatField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return f"{self.id} {self.type} {self.ph} {self.district}"

class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    pnumber = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} {self.fname} {self.laname} {self.email} {self.password} {self.pnumber}"


class PostMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.user} {self.message} {self.date}"

class ReplyMessage(models.Model):
    PostMessage = models.ForeignKey(PostMessage, on_delete=models.CASCADE)
    reply = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.PostMessage} {self.reply} {self.date}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.user} {self.comment} {self.date}"
    
class AnalyzedData(models.Model):
    date = models.DateTimeField(auto_now=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    sowing = models.BooleanField()
    harvesting = models.BooleanField()

    def __str__(self):
        return f"{self.id} {self.date} {self.district} {self.sowing}, {self.harvesting}"


    