from django.conf.urls import patterns, url
from account_app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register$','account_app.views.register', name='register'),
        url(r'^login$','account_app.views.login', name='login'),
        url(r'^logout$','account_app.views.logout', name='logout'),
)