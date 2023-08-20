from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 
    
