from django.db import models

class classificationTable(models.Model):
    age = models.FloatField(null=True, blank=True)  
    gender = models.FloatField(null=True, blank=True)
    impulse = models.FloatField(null=True, blank=True)
    pressurehigh = models.FloatField(null=True, blank=True)
    pressurelow = models.FloatField(null=True, blank=True)
    glucose = models.FloatField(null=True, blank=True)
    kcm = models.FloatField(null=True, blank=True)
    troponin = models.FloatField(null=True, blank=True)
    classification = models.FloatField(null=True, blank=True)
 
class regressionTable(models.Model):
    carat = models.FloatField(null=True, blank=True)  
    cut = models.FloatField(null=True, blank=True)
    color = models.FloatField(null=True, blank=True)
    clarity = models.FloatField(null=True, blank=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    z = models.FloatField(null=True, blank=True)  
