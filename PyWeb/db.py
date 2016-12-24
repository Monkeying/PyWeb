# -*- coding: utf-8 -*-

from django.http import HttpResponse

from PyWebApp.models import UserForm

# 数据库操作
def db_addUser(request):
	test1 = UserForm(userName= "Alex", userPassword = request.get_full_path().split('?')[1])#you are able to getdata from url by get_full_path().split
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")

def db_SearchUser(request):
	try:
		user = UserForm.objects.get( userName = "Alex",  userPassword = request.get_full_path().split('?')[1])
	except:
		return HttpResponse("fuck")
	return HttpResponse(user)


def get_or_create(cls, **kwargs):
	try:
		instance, created = cls.get(**kwargs), False
	except cls.DoesNotExist:
		instance, created = cls.create(**kwargs), True
	return instance, created

