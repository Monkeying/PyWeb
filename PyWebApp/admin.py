from django.contrib import admin

from PyWebApp.models import UserForm
from PyWebApp.models import DeviceForm
# Register your models here.
admin.site.register(UserForm)
admin.site.register(DeviceForm)