from __future__ import unicode_literals

from django.db import models

class accidentData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    severity = models.IntegerField(default=1)

    def __str__(self):
        return "lat:{0}  long:{1}  severity:{2}".format(self.latitude, self.longitude, self.severity)

# Create your models here.
