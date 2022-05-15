from django.db import models

# Create your models here.
class feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class contactus(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.name

class booking(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    booking_time=models.DateTimeField()
    people=models.IntegerField()
    req=models.TextField()
