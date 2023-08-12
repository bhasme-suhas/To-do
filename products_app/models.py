from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    
    
