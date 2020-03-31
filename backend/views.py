from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from datetime import datetime
from django.http import HttpResponse
from django.core import serializers
import csv
# Create your views here.

def get_data(request, sdate, edate):
	sd = datetime.strptime(str(sdate), '%Y-%m-%d')
	ed = datetime.strptime(str(edate), '%Y-%m-%d')
	query = Data.objects.filter(timeStamp__gte= sd, timeStamp__lte=ed).values()
	query1 = Data.objects.filter(timeStamp__gte= sd, timeStamp__lte=ed)
	data = serializers.serialize("xml", query1)
	print(data)
	return JsonResponse({"data" : list(query)})
	#print(query)
	#return HttpResponse(d)

def add_data(request):
            with open('./data2frommongo.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
            
                for f in reader:
                    ts = f['Time_Stamp']
                    oid = f['_id']
                    current = f['Current']
                    voltage = f['voltage']
                    power_factor = f['Power_Factor']

                    Data.objects.create(uid = oid, timeStamp=ts, current=current, voltage=voltage, powerFactor = power_factor)

            return render(request, "add_students.html", {})