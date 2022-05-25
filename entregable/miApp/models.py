from django.db import models

# Create your models here.
class entryModel(models.Model):
    dateTime = models.DateTimeField()
    concept = models.CharField(max_length=255)
    value = models.FloatField()
    