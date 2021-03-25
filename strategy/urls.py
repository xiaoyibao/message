# encoding: utf-8

"""Message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
'''
@author: leon
@project: Message
@created: 2018/10/15 9:39
@ide: PyCharm
@url: www.sinosoft.com.cn
@desc: a file named urls.py in Message
'''
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from strategy.views import *

router = DefaultRouter()
router.register(r'receptor', ReceptorViewSet)
router.register(r'group', GroupViewSet)
router.register(r'relation', RelationViewSet)
router.register(r'strategy', StrategyViewSet)
router.register(r'log', LogViewSet)
# router.register(r'snippets', views.SnippetViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]