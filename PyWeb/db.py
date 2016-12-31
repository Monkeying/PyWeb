# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render

from PyWebApp.models import UserForm
from PyWebApp.models import DeviceForm

from PyWeb import SocketServer



import json

import urllib.parse

import sched,time

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
changedDevId = []
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


def userLogin(request):
	#try:
		print (request.POST.getlist("userName"))

		data_raw  = request.POST
		data = json.loads(next(data_raw.lists())[0])
		print(data)
		result = UserForm.objects.get(userName=request.GET["userName"], userPassword=request.GET["userPassword"],)
		url = "users.html?userId=" + result.id
		return render(request,url)
	#except:
		return HttpResponse("{'result':false}")
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
		HttpResponse("SOMTHING WRONG")
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

def db_SearchUser(email,name,password):
	try:
		user = UserForm.objects.all().get(userName=name,userPassword=password,userEmail=email)
		return user.id
	except:
		return -1

def table(request):
	print("table")
	user = UserForm.objects.get(id = request.GET["userId"])
	print(user.id)
	for dev in user.deviceform_set.all():
		print(dev.id)
		changedDevId.append(dev.id)
	return render(request,"tables.html")
def serverKeepUpdate(request):
	#	event = sched.scheduler(time.time, time.sleep)
#	file = open("templates/tables/data1.json","r")
#	obj = file.read()
#	data = json.loads(obj)
#	data = []
#	obj = json.dumps(data)
	while True:
		if (changedDevId):
			response = []
			print (request.GET)
			user = UserForm.objects.get(id= request.GET["userId"])
			for device in user.deviceform_set.all():
				print(device.id)
				deviceInfo = {}
				for name in DeviceForm._meta.fields:
					name = str(name)
					name = name.split(".")[2]
					deviceInfo[name] = getattr(device, name)
				if device.id in changedDevId:
					response.insert(0,deviceInfo)
				else:
					response.append(deviceInfo)

			changedDevId.clear()

			responseJSON = json.dumps(response)
			return HttpResponse(responseJSON)

"""
def serverKeepUpdate(request):
#	event = sched.scheduler(time.time, time.sleep)
	while True:
		if ( changedDevId ):
			response = {}
			for devId in changedDevId: #data format {'Id':{'SN':asdf,'Name':asd},'Id':{'SN':sad}}
				device = DeviceForm.objects.get(id=devId)
				deviceInfo = {}
				for user in device.users.all():
					if str(user.id) == request.GET["userId"]:
						for name in  DeviceForm._meta.fields:
							name = str(name)
							name = name.split(".")[2]
							deviceInfo[name] = getattr(device,name)
				response[devId] = deviceInfo
				changedDevId.remove(devId)

			changedDevId.clear()

			responseJSON = json.dumps(response)
			return HttpResponse(responseJSON)

#		else:
#			event.enter(10,2,serverKeepUpdate)
"""
def validate(request):
	userId = db_SearchUser(request.POST["email"],request.POST["name"],request.POST["password"])
	if (userId != -1):
		url = "index.html/?userId=" + str(userId)
		return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect("/?0")

def devUpdate(request):
	print (request.POST)
	device = DeviceForm.objects.get(id=request.POST["deviceId"])
	nameList = dir(device)
	for name in nameList:
		print(name+request.POST[name])
		setattr(device,name,request.POST[name])

	return HttpResponse("{'result':'done'}")



def userSocket(request):
	print (request)
	return HttpResponse("back")

def serverSocket(request):
	#try:
		server= SocketServer.WebSocketServer()
		print("begin")
		server.begin()
		print ("here")
	#except:
		print ("wrong")
		return HttpResponse("hi")
