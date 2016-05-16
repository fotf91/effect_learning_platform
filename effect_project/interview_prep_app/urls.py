from django.conf.urls import patterns, url
from interview_prep_app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # url(r'^questions/(?P<interview_level>[\w\-]+)/$', 'interview_prep_app.views.questions', name='questions'),
                       url(r'^questions/(?P<interview_level>[\w\-]+)/(?P<question_num>[0-9]{2})/$', 'interview_prep_app.views.questions', name='questions'),
                       # url(r'^summary', 'interview_prep_app.views.summary', name='summary'),
                       url(r'^summary/(?P<interview_level>[\w\-]+)/$', 'interview_prep_app.views.summary', name='summary'),
                       )