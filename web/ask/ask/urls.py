from django.conf.urls import url
from django.contrib import admin
from qa.views import test, basetemp, questpage

urlpatterns = [
	url(r'^$', basetemp, {'url':'/?page=','order':'-added_ad'}),
	url(r'^login/.*$', test),
	url(r'^signup/.*$', test),
	url(r'^question/(?P<slug>\d+)/$', questpage),
	url(r'^ask/.*$', test),
	url(r'^popular/.*$', basetemp, {'url':'/popular/?page=','order':'-likes'}),
	url(r'^new/.*$', test),
]
