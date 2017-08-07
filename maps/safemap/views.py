from django.shortcuts import render
import csv
from models import accidentData
from haversine import haversine

def details(request):
    return render(request, 'safemap/geocode.html',)


def results(request):
    age = int(request.POST.get('age'))
    expertise = int(request.POST.get('experience'))
    gender = request.POST.get('gender')
    lat = float(request.POST.get('latitude'))
    long = float(request.POST.get('longitude'))

    distList = []
    severity = []

    for data in accidentData.objects.all():
        dist = haversine((lat, long), (data.latitude, data.longitude))
        distList.append(dist)
        severity.append(data.severity)

    severityvalue = (severity[distList.index(min(distList))]+(6-expertise))/2

    if severityvalue in range(1, 2):
        message = "Very safe"
    elif severityvalue in range(2, 3):
        message = "Quite safe"
    elif severityvalue in range(3, 4):
        message = "Drive with precaution"
    elif severityvalue in range(4, 6):
        message = "Accident Zone!"
    return render(request, 'safemap/verdict.html', context={'message': message})


def uploadData():
    csvreader = csv.reader(open('safemap/accident.csv'), delimiter=',')
    for row in csvreader:
        data = accidentData()
        data.latitude = float(row[1])
        data.longitude = float(row[0])
        data.severity = int(row[11])
        data.save()






