from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=50)
    tracks_lat = models.FloatField()
    tracks_long = models.FloatField()


class Exit(models.Model):
    number = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="exit")


