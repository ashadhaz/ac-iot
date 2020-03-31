from django.db import models

# Create your models here.

class Data(models.Model):
	uid = models.CharField(max_length=50, blank=True, null=True)
	timeStamp = models.DateTimeField(blank=True, null=True)
	deviceID = models.IntegerField(blank=True, null=True)
	current = models.FloatField(blank=True, null=True)
	voltage = models.FloatField(blank=True, null=True)
	powerFactor = models.FloatField(blank=True, null=True)
	room_temp = models.FloatField(blank=True, null=True)
	Compressor_temp =models.FloatField(blank=True, null=True)
	External_temp= models.FloatField(blank=True, null=True)
	Current_mode_of_AC = models.CharField(max_length=10, blank=True, null=True)
	AC_fan = models.CharField(max_length=3, blank=True, null=True)
	AC_brand = models.CharField(max_length=50, blank=True, null=True)
	Humidity = models.FloatField(blank=True, null=True)
	updated = models.DateTimeField(blank=True, null=True)
	created = models.DateTimeField(blank=True, null=True)
	etag = models.CharField(max_length=50, blank=True, null=True)
