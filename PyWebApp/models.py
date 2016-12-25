from django.db import models

# Create your models here.

class UserForm(models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)

    def __getDevices__(self):
        return self.deviceform_set.all() #return a list
    def __addDevice__(self,dev):
        self.deviceform.set.add(dev)

class DeviceForm(models.Model):
    users = models.ManyToManyField(UserForm, null=True)
    deviceName = models.CharField(max_length=20)
    SN = models.CharField(max_length=20)
    tempreture = models.CharField(max_length=20)
    lastUpdateTime = models.CharField(max_length=20)
    alarm = models.CharField(max_length=20)

    def __getUsers__(self):
        return self.users.all() #return a list

    def __addUser__(self,user):
        self.users.add(user)