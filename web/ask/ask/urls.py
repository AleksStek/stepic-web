from django.conf.urls import url
from django.contrib import admin
from qa.views import test, basetemp, questpage, askform, newanswer, questempty

urlpatterns = [
	url(r'^$', basetemp, {'url':'/?page=','order':'-added_ad'}),
	url(r'^login/.*$', test),
	url(r'^signup/.*$', test),
	url(r'^question/(?P<slug>\d+)/$', questpage),
	url(r'^question/$', questempty),
	url(r'^ask/.*$', askform),
	url(r'^popular/.*$', basetemp, {'url':'/popular/?page=','order':'-likes'}),
	url(r'^new/.*$', test),
	url(r'^answer/.*$', newanswer),
]
