from django.db import models
from django.utils import timezone
# Create your models here.


class smartphone(models.Model):
    name= models.CharField(max_length=120)
    price= models.IntegerField()
    link_img=models.URLField()
    link_url=models.URLField(default="None")

    def __str__(self):
        return self.name

