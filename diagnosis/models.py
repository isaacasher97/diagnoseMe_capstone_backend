from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    specialist = models.CharField(max_length=200)
    practiceType = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
