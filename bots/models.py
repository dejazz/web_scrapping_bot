from django.db import models

class Bot(models.Model):
     description = models.TextField()
     hdd = models.TextField()
     hdd_unavailable = models.TextField()
     product_id = models.CharField(max_length=20)
     price = models.CharField(max_length=20)
     reviews = models.CharField(max_length=50)
     starts = models.IntegerField()
     product_infos = models.CharField(max_length=256)
     
     ...
  
