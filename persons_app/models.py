from django.db import models

# Create your models here.

class Persons(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    