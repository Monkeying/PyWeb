# -*- coding: utf-8 -*-

from django.http import HttpResponse

from PyWebApp.models import UserForm
from PyWebApp.models import DeviceForm

import json

import urllib.parse

"""
	data = request.get_full_path().split("?")[1]
	url = urllib.parse.unquote(data) #将url中的转义部分如引号转移为%22 重新转义为字符串
	dataJSON = json.loads(url) #将字符串转义为JSON格式
	print(dataJSON)
"""
# 数据库操作

"""
	url0 = request.get_full_path().split("?")[1]
	url1 = urllib.parse.unquote(url0)  # 将url中的转义部分如引号转移为%22 重新转义为字符串
	data = json.loads(url1)  # 将字符串转义为JSON格式

"""
def dataClear(request):
	if request.method == 'GET':
		data_raw =  request.GET
	elif request.method == 'POST':
		data_raw = request.POST
	else:
		print (request.method)
		return HttpResponse("{'result':WRONG METHOD:" + request.method + "'")
	print (request.META)
	data = json.loads( next( data_raw.lists() )[0] )
	print (data)

	if data["operation"] == "userSignUp":
		return HttpResponse(userSignUp(data))
	elif data["operation"] == "deviceSignUp":
		deviceSignUp(data)
	elif data["operation"] == "userSignIn":
		userSignIn(data)
	elif data["operation"] == "devSignIn":
		devSignIn(data)
	elif data["operation"] == "addDev":
		UserForm.objects.get(id=data["userId"]).__addDevice__(DeviceForm.objects.get(id=data["devId"]))
	elif data["operation"] == "addUser":
		DeviceForm.objects.get(id=data["devId"]).__addUser__(UserForm.objects.get(id=data["userId"]))
	elif data["operation"] == "devUpdate":
		devUpdate(data)
	elif data["operation"] == "userUpdate":
		userUpdate(data)
	else:
		print (data["operation"])
		return HttpResponse("{'result':'wrong operation'}")

	return HttpResponse("{'result':'yes'}")

def userUpdate(data):
	devices = UserForm.objects.get(id=data["userId"]).deviceform_set.all() #get a list of devices of this user
	response = []
	for i in range (0,len(devices)):
		device = {}
		device["SN"] = devices[i].SN

		response.append(device)
	return HttpResponse(json.loads(response))

def devUpdate(data):
	device = DeviceForm.objects.get(id=data["devId"])
	device.SN = data["SN"]

	return HttpResponse("{'result':'done'}")
def userSignUp(data):
	#try:
		print (data["userName"]+data["userPassword"])
		obj,created = UserForm.objects.get_or_create(userName=data["userName"], userPassword=data["userPassword"],)
		print ("1")
		if created == False: #does not exist and created one
			print("2")
			user = obj # the creating one
			return HttpResponse("THIS HAS BEEN REGISTERED")
		else:
			print("3")
			return HttpResponse("Successfully registered")
	#except:
		print ("except in userSignUp")
		HttpResponse("SOMTHING WROING")
		return False
def deviceSignUp(data):
	try:
		result = UserForm.objects.get_or_create(DeviceName=data["DeviceName"],SN=data["SN"])
		if result[1] == False: #does not exist and created one
			user = result[0] # the creating one
			return HttpResponse("Successfully registered")
		else:
			return HttpResponse("This device has been registered")
	except:
		print ("except in userSignUp")
		HttpResponse("SOMTHING WROING")
		return False

def db_SearchUser(request):
	try:
		user = UserForm.objects.get( userName = "Alex",  userPassword = request.get_full_path().split('?')[1])
	except:
		return HttpResponse("fuck")
	return HttpResponse(user)


def get_or_create(request):
	try:
		instance, created = cls.get(**kwargs), False
	except cls.DoesNotExist:
		instance, created = cls.create(**kwargs), True
	return instance, created

def User_get_or_create(request):
	data = request.get_full_path().split("?")[1]
	url = urllib.parse.unquote(data)
	print (url)
	dataJSON = json.loads(url)
	print (dataJSON)
	name = dataJSON["userName"]
	password = dataJSON["userPassword"]
	print (name + password)
	try:
		user = UserForm.objects.filter(userName=dataJSON["userName"], userPassword=dataJSON["userPassword"])
		print ("try")
		if user[0].devices:
			print ("yes")
		else:
			print ("no")
		print (type(user[0].devices))
		for i in range (0, len(user)):
			userJSON = {"SN":user[i].devices.SN,"name":user[i].devices.deviceName}
			userStr = str(userJSON)
			print (userStr)
	except:
		print("except")
		newUser = UserForm(userName=dataJSON["userName"], userPassword=dataJSON["userPassword"],devices = DeviceList.objects.get(id=6))
		newUser.save()
		return HttpResponse("fucking worked")
	return HttpResponse(userStr)
