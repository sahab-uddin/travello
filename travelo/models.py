from django.db import models

# Create your models here.
class Destination(models.Model):
    
    price = models.IntegerField()
    desc = models.TextField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)