from django.db import models

# Create your models here.
class deviceList(models.Model):
    deviceName = models.CharField(max_length=20)
    SN = models.CharField(max_length=20)
    tempreture = models.CharField(max_length=20)
    lastUpdateTime = models.CharField(max_length=20)
    alarm = models.CharField(max_length=20)

class UserForm(models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    inners = [deviceList]