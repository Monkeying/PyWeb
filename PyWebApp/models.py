from django.db import models

# Create your models here.

class UserForm(models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length=20)

    def __getDevices__(self):
        return self.deviceform_set.all() #return a list
    def __addDevice__(self,dev):
        self.deviceform.set.add(dev)

class DeviceForm(models.Model):
    users = models.ManyToManyField(UserForm)
    deviceName = models.CharField(max_length=20,blank=True)
    SN = models.CharField(max_length=20,blank=True)
    temperature = models.CharField(max_length=20,blank=True)
    lastUpdateTime = models.CharField(max_length=20,blank=True)
    alarm = models.CharField(max_length=20,blank=True)
    history = models.TextField(blank=True)

    def __getUsers__(self):
        return self.users.all() #return a list

    def __addUser__(self,user):
        self.users.add(user)