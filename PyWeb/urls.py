"""PyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django import views
admin.autodiscover()

from PyWeb import view
from PyWeb import db
from PyWeb import settings

urlpatterns = [
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_PATH}),

#    url(r'^static/(?P<path>.*)$', include('document_root': settings.STATIC_ROOT}, name='static'),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', view.Login),
    url(r'^user/keepUpdate',db.serverKeepUpdate),
    url(r'^user/validate',db.validate),
    url(r'^device/update',db.devUpdate),

    url(r'^user/index.html',view.index),
    url(r'^user/tables.html',db.table),
    url(r'^user/tables/data1.json',db.serverKeepUpdate),

    url(r'^user/Login',db.userLogin),

]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()