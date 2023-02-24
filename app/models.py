from django.db import models

# Create your models here.

class Topic(models.Model):
    tn=models.CharField(max_length=50)
   