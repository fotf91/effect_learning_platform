from django.conf.urls import patterns, url
from interview_prep_app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^questions$', 'interview_prep_app.views.questions', name='questions'),
                       )