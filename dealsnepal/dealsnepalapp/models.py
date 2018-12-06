from django.db import models

# Create your models here.


class smartphone(models.Model):
    name= models.CharField(max_length=120)
    price= models.IntegerField()
    link=models.URLField()

    def __self__(self):
        return self.name

